from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models import db, User
from functools import wraps
from urllib.parse import urlparse
import jwt
import datetime
import os
import uuid

# ---------------------------------------------------------
# Blueprint + config
# ---------------------------------------------------------

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

# Kept for backwards compatibility in your codebase:
PUBLIC_BASE_URL = os.getenv("FLASK_PUBLIC_BASE_URL", "http://localhost:5000")

ALLOWED_EXT = {"png", "jpg", "jpeg", "webp"}

# ---------------------------------------------------------
# JWT helpers
# ---------------------------------------------------------


def create_jwt(user_id: str, email: str) -> str:
    payload = {
        "id": user_id,  # UUID string
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_jwt(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])


def get_bearer_token():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    return auth.split(" ", 1)[1].strip()


def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = get_bearer_token()
        if not token:
            return jsonify({"error": "Missing Authorization header"}), 401

        try:
            payload = decode_jwt(token)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        user_id = payload.get("id")
        if not user_id:
            return jsonify({"error": "Invalid token payload"}), 401

        user = db.session.get(User, user_id)  # best practice on modern SQLAlchemy
        if not user:
            return jsonify({"error": "User not found"}), 401

        # Attach user to request
        request.user = user
        return f(*args, **kwargs)

    return wrapper


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


def delete_old_avatar(user: User):
    if not user.image:
        return

    path = user.image

    # If it's an absolute URL, strip to path
    if path.startswith("http://") or path.startswith("https://"):
        try:
            path = urlparse(path).path
        except Exception:
            return

    # Only delete locally stored avatars
    if not path.startswith("/static/uploads/avatars/"):
        return

    avatar_path = os.path.join(current_app.root_path, path.lstrip("/"))

    try:
        if os.path.exists(avatar_path):
            os.remove(avatar_path)
    except Exception as e:
        current_app.logger.warning(f"Failed to delete avatar: {e}")


def ensure_linked(user: User, provider: str):
    """Ensure provider exists in linked_accounts (case-insensitive)."""
    linked = user.linked_accounts or []
    lower = {x.lower() for x in linked}
    if provider.lower() not in lower:
        # Assign a new list object (extra-safe even with MutableList)
        user.linked_accounts = linked + [provider]


def public_image_url(image_value: str | None) -> str | None:
    """
    Return an absolute URL for locally-stored avatar paths at response time,
    without changing what's stored in the DB.

    - If image_value is already absolute (OAuth/CDN), return as-is.
    - If image_value is a relative path like /static/..., prefix with FLASK_BACKEND_API (preferred)
      or FLASK_PUBLIC_BASE_URL as fallback.
    """
    if not image_value:
        return None

    if image_value.startswith("http://") or image_value.startswith("https://"):
        return image_value

    base = (PUBLIC_BASE_URL or PUBLIC_BASE_URL or "").rstrip("/")
    if not base:
        return image_value

    path = image_value if image_value.startswith("/") else f"/{image_value}"
    return f"{base}{path}"


def auth_response(user: User):
    token = create_jwt(user.id, user.email)
    data = user.to_dict()

    # Only modify the outgoing payload (do NOT write back to DB)
    data["image"] = public_image_url(data.get("image"))
    data["accessToken"] = token
    
    return jsonify(data), 200


# ---------------------------------------------------------
# SIGNUP (email + password)
# ---------------------------------------------------------


@auth_bp.post("/signup")
def signup():
    """
    Sign up with email + password
    ---
    tags:
      - auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [email, password]
          properties:
            email:
              type: string
              example: test@example.com
            password:
              type: string
              example: mypassword123
            username:
              type: string
              example: ataylor
    responses:
      200:
        description: User object + accessToken
      400:
        description: Missing email or password
      409:
        description: Email already registered
    """
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")
    username = data.get("username") or (email.split("@")[0] if email else None)

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    if User.query.filter_by(email=email).first():
        return (
            jsonify(
                {
                    "error": "This email is already registered. Please log in or set a password from your profile."
                }
            ),
            409,
        )

    user = User(
        email=email,
        username=username or email.split("@")[0],
        password=generate_password_hash(password),
        linked_accounts=["credentials"],
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    return auth_response(user)


# ---------------------------------------------------------
# LOGIN (email + password)
# ---------------------------------------------------------


@auth_bp.post("/login")
def login():
    """
    Log in with email + password
    ---
    tags:
      - auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [email, password]
          properties:
            email:
              type: string
              example: test@example.com
            password:
              type: string
              example: mypassword123
    responses:
      200:
        description: User object + accessToken
      401:
        description: Invalid credentials / no password set
    """
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.password:
        return (
            jsonify(
                {
                    "error": "No password set for this account. Please log in using OAuth and set one in settings."
                }
            ),
            401,
        )

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    return auth_response(user)


# ---------------------------------------------------------
# SET / CHANGE PASSWORD
# ---------------------------------------------------------


@auth_bp.post("/set-password")
@require_auth
def set_password():
    """
    Set or change password (requires Bearer token)
    ---
    tags:
      - auth
    security:
      - BearerAuth: []
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [new_password]
          properties:
            new_password:
              type: string
              example: newpassw0rd!
            current_password:
              type: string
              example: oldpassw0rd!
    responses:
      200:
        description: Updated user object + new accessToken
      400:
        description: Validation error
      401:
        description: Unauthorized / incorrect current password
    """
    data = request.get_json() or {}
    new_password = data.get("new_password")
    current_password = data.get("current_password")

    user: User = request.user

    if not new_password or len(new_password) < 8:
        return jsonify({"error": "Password must be at least 8 characters."}), 400

    if user.password:
        if not current_password:
            return jsonify({"error": "Current password required."}), 400
        if not check_password_hash(user.password, current_password):
            return jsonify({"error": "Current password incorrect."}), 401

    user.password = generate_password_hash(new_password)
    ensure_linked(user, "credentials")

    db.session.commit()
    db.session.refresh(user)
    return auth_response(user)


@auth_bp.post("/set-username")
@require_auth
def set_username():
    data = request.get_json() or {}
    username = data.get("username")

    user: User = request.user

    if not username:
        return jsonify({"error": "No username sent"}), 400

    user.username = username
    db.session.commit()
    db.session.refresh(user)
    return auth_response(user)


# ---------------------------------------------------------
# OAUTH SYNC (NextAuth)
# ---------------------------------------------------------


@auth_bp.post("/sync-user")
def sync_user():
    data = request.get_json() or {}
    email = data.get("email")
    provider = data.get("provider")
    name = data.get("name")
    image = data.get("image")

    if not email or not provider:
        return jsonify({"error": "Missing email or provider"}), 400

    provider = provider.lower()

    user = User.query.filter_by(email=email).first()

    if user:
        linked = user.linked_accounts or []

        # must already be linked, otherwise block (your existing logic)
        if provider not in {x.lower() for x in linked}:
            return (
                jsonify(
                    {
                        "error": f"This email is already registered. "
                        f"Please log in normally and link {provider.capitalize()} from settings."
                    }
                ),
                403,
            )

        if not user.username and name:
            user.username = name
        if not user.image and image:
            user.image = image

        db.session.commit()
        db.session.refresh(user)
        return auth_response(user)

    # Create new OAuth user
    user = User(
        email=email,
        username=name or email.split("@")[0],
        image=image,
        linked_accounts=[provider],
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    return auth_response(user)


# ---------------------------------------------------------
# MANUAL PROVIDER LINK
# ---------------------------------------------------------


@auth_bp.post("/link-provider")
def link_provider():
    data = request.get_json() or {}
    user_email = data.get("user_email")
    provider_email = data.get("provider_email")
    provider = data.get("provider")

    if not user_email or not provider_email or not provider:
        return jsonify({"error": "Missing fields"}), 400

    provider = provider.lower()

    main_user = User.query.filter_by(email=user_email).first()
    if not main_user:
        return jsonify({"error": "Main account not found"}), 404

    oauth_user = User.query.filter_by(email=provider_email).first()

    if oauth_user and oauth_user.id != main_user.id:
        merged_lower = {x.lower() for x in (main_user.linked_accounts or [])}
        merged_lower |= {x.lower() for x in (oauth_user.linked_accounts or [])}
        merged_lower.add(provider)

        # store canonical lowercase providers
        main_user.linked_accounts = sorted(list(merged_lower))

        if oauth_user.image and not main_user.image:
            main_user.image = oauth_user.image
        if oauth_user.username and not main_user.username:
            main_user.username = oauth_user.username

        db.session.delete(oauth_user)
    else:
        ensure_linked(main_user, provider)

    db.session.commit()
    db.session.refresh(main_user)
    return auth_response(main_user)


# ---------------------------------------------------------
# PROFILE IMAGE UPLOAD
# ---------------------------------------------------------


@auth_bp.post("/set-image")
@require_auth
def set_image():
    """
    Set or change password (requires Bearer token)
    ---
    tags:
      - auth
    security:
      - BearerAuth: []
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [new_password]
          properties:
            new_password:
              type: string
              example: newpassw0rd!
            current_password:
              type: string
              example: oldpassw0rd!
    responses:
      200:
        description: Updated user object + new accessToken
      400:
        description: Validation error
      401:
        description: Unauthorized / incorrect current password
    """
    user: User = request.user

    if "image" not in request.files:
        return jsonify({"error": "Missing file field 'image'"}), 400

    f = request.files["image"]
    if not f or f.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(f.filename):
        return jsonify({"error": "Invalid file type"}), 400

    # Ensure upload folder exists
    upload_dir = os.path.join(current_app.root_path, "static", "uploads", "avatars")
    os.makedirs(upload_dir, exist_ok=True)

    delete_old_avatar(user)

    ext = f.filename.rsplit(".", 1)[1].lower()
    filename = secure_filename(f"{uuid.uuid4().hex}.{ext}")
    file_path = os.path.join(upload_dir, filename)
    f.save(file_path)

    # Store as a RELATIVE path so base URL can change later without reupload
    user.image = f"/static/uploads/avatars/{filename}"
    db.session.commit()
    db.session.refresh(user)

    return auth_response(user)
