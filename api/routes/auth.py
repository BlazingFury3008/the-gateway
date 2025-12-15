from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
import jwt
import datetime
import os

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

from functools import wraps

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

        user = User.query.get(payload.get("id"))
        if not user:
            return jsonify({"error": "User not found"}), 401

        # Attach to request context (simple + effective)
        request.user = user
        return f(*args, **kwargs)
    return wrapper


# ---------------------------------------------------------
# Helper: create JWT
# ---------------------------------------------------------
def create_jwt(user_id, email):
    payload = {
        "id": user_id,
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# ---------------------------------------------------------
# SIGNUP (email + password)
# ---------------------------------------------------------
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    username = data.get("username", email.split("@")[0])

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    existing = User.query.filter_by(email=email).first()

    if existing:
        # ❌ Do NOT allow signup when OAuth account exists
        return jsonify({
            "error": "This email is already registered. Please log in using that method or add a password from your profile."
        }), 409

    hashed_pwd = generate_password_hash(password)
    user = User(
        email=email,
        username=username,
        password=hashed_pwd,
        linked_accounts=["credentials"],
    )
    db.session.add(user)
    db.session.commit()

    token = create_jwt(user.id, user.email)
    user_data = user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200


# ---------------------------------------------------------
# LOGIN (email + password)
# ---------------------------------------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.password:
        return jsonify({"error": "No password set for this account. Please log in with Discord/Google, then set a password in settings."}), 401

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_jwt(user.id, user.email)
    user_data = user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200


@auth_bp.route("/set-password", methods=["POST"])
@require_auth
def set_password():
    """
    Set password for an OAuth-only account OR change existing password.

    Request JSON:
      - new_password (required)
      - current_password (required only if user already has a password)
    """
    data = request.get_json() or {}
    new_password = data.get("new_password")
    current_password = data.get("current_password")

    user: User = request.user

    if not new_password or len(new_password) < 8:
        return jsonify({"error": "Password must be at least 8 characters."}), 400

    already_has_password = bool(user.password)

    # If changing existing password, verify current
    if already_has_password:
        if not current_password:
            return jsonify({"error": "Current password is required to change your password."}), 400
        if not check_password_hash(user.password, current_password):
            return jsonify({"error": "Current password is incorrect."}), 401

    user.password = generate_password_hash(new_password)

    linked = user.linked_accounts or []
    linked_lower = {str(x).lower() for x in linked}
    if "credentials" not in linked_lower:
        linked.append("credentials")
        user.linked_accounts = linked

    db.session.commit()

    token = create_jwt(user.id, user.email)
    user_data = user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200


# ---------------------------------------------------------
# SYNC USER (OAuth auto-link or conflict return)
# ---------------------------------------------------------
@auth_bp.route("/sync-user", methods=["POST"])
def sync_user():
    """
    Called by NextAuth after OAuth login.

    Behavior:
      ✔ If account DOES exist (same email)
         - If provider already linked → Login OK
         - If provider NOT linked → return 403 (user must manually link)

      ✔ If account does NOT exist → create new OAuth user
    """
    data = request.get_json()
    email = data.get("email")
    provider = data.get("provider")
    name = data.get("name")
    image = data.get("image")

    if not email or not provider:
        return jsonify({"error": "Missing email or provider"}), 400

    user = User.query.filter_by(email=email).first()

    # ------------------------------------------------------------------
    # CASE 1: Existing user found
    # ------------------------------------------------------------------
    if user:
        linked = user.linked_accounts or []

        # Provider NOT linked yet → require manual linking (403)
        if provider not in linked:
            return jsonify({
                "error": f"This email is already registered via another login method. "
                         f"Please log in normally and manually link {provider.capitalize()} "
                         f"from your profile settings."
            }), 403

        # Provider is linked → update fields if missing and allow login
        if not user.username and name:
            user.username = name
        if not user.image and image:
            user.image = image

        db.session.commit()

        token = create_jwt(user.id, user.email)
        user_data = user.to_dict()
        user_data["accessToken"] = token
        return jsonify(user_data), 200

    # ------------------------------------------------------------------
    # CASE 2: No account exists → create new OAuth user
    # ------------------------------------------------------------------
    user = User(
        email=email,
        username=name or email.split("@")[0],
        image=image,
        linked_accounts=[provider],
    )
    db.session.add(user)
    db.session.commit()

    token = create_jwt(user.id, user.email)
    user_data = user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200


# ---------------------------------------------------------
# LINK PROVIDER (manual linking, emails may differ)
# ---------------------------------------------------------
@auth_bp.route("/link-provider", methods=["POST"])
def link_provider():
    """
    Allows linking ANY provider to ANY user,
    even when emails differ.
    """
    data = request.get_json()
    user_email = data.get("user_email")
    provider_email = data.get("provider_email")
    provider = data.get("provider")

    if not user_email or not provider_email or not provider:
        return jsonify({"error": "Missing fields"}), 400

    main_user = User.query.filter_by(email=user_email).first()
    if not main_user:
        return jsonify({"error": "Main account not found"}), 404

    # If there is a separate OAuth account, merge them
    oauth_user = User.query.filter_by(email=provider_email).first()

    if oauth_user and oauth_user.id != main_user.id:
        merged = list(set(main_user.linked_accounts + oauth_user.linked_accounts + [provider]))
        main_user.linked_accounts = merged

        if oauth_user.image and not main_user.image:
            main_user.image = oauth_user.image
        if oauth_user.username and not main_user.username:
            main_user.username = oauth_user.username

        db.session.delete(oauth_user)
        db.session.commit()
    else:
        linked = main_user.linked_accounts or []
        if provider not in linked:
            linked.append(provider)
            main_user.linked_accounts = linked
        db.session.commit()

    token = create_jwt(main_user.id, main_user.email)
    user_data = main_user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200
