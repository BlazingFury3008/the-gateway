from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
import jwt
import datetime
import os

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "supersecretkey")

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
        # If user already exists, just return their data (no duplicate)
        token = create_jwt(existing.id, existing.email)
        user_data = existing.to_dict()
        user_data["accessToken"] = token
        return jsonify(user_data), 200

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
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_jwt(user.id, user.email)
    user_data = user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200


# ---------------------------------------------------------
# SYNC USER (OAuth auto-link)
# ---------------------------------------------------------
@auth_bp.route("/sync-user", methods=["POST"])
def sync_user():
    """
    Called by NextAuth after OAuth login.
    - Links provider if user exists
    - Creates a new user otherwise
    - Updates username/image if previously missing
    """
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    provider = data.get("provider")
    image = data.get("image")

    if not email or not provider:
        return jsonify({"error": "Missing email or provider"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        # --- Create new user from OAuth ---
        user = User(
            email=email,
            username=name or email.split("@")[0],
            image=image,
            linked_accounts=[provider],
        )
        db.session.add(user)
    else:
        # --- Existing user: update missing info ---
        linked = user.linked_accounts or []
        if provider not in linked:
            linked.append(provider)
            user.linked_accounts = linked

        # Fill in missing username if blank/null
        if not user.username and name:
            user.username = name

        # Add image if not already set or empty
        if not user.image and image:
            user.image = image

    db.session.commit()

    token = create_jwt(user.id, user.email)
    user_data = user.to_dict()
    user_data["accessToken"] = token
    return jsonify(user_data), 200


# ---------------------------------------------------------
# LINK PROVIDER (manual link from profile)
# ---------------------------------------------------------
@auth_bp.route("/link-provider", methods=["POST"])
def link_provider():
    """
    Called when a logged-in user manually links a provider
    from their account page.
    Expects: user_email (main account), provider_email, provider
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

    existing = User.query.filter_by(email=provider_email).first()
    if existing and existing.id != main_user.id:
        # Merge duplicate OAuth account into main
        merged_accounts = list(
            set(main_user.linked_accounts + existing.linked_accounts + [provider])
        )
        main_user.linked_accounts = merged_accounts
        if existing.image and not main_user.image:
            main_user.image = existing.image
        if existing.username and not main_user.username:
            main_user.username = existing.username
        db.session.delete(existing)
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
