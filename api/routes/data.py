import os
from flask import Blueprint, request, jsonify
from models import db, User, Character

# Optional safety net: loads .env if python-dotenv is installed.
# This prevents "not configured" when the app doesn't auto-load env files.
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

# ---------------------------------------------------------
# Blueprint + config
# ---------------------------------------------------------
data_bp = Blueprint("data", __name__, url_prefix="/data")


# ---------------------------------------------------------
# API Key auth
# ---------------------------------------------------------
def require_api_key():
    """Return (json, status) if unauthorized, otherwise None."""
    # ✅ read env at call-time (not import-time)
    data_api_key = os.getenv("DATA_API_KEY")

    if not data_api_key:
        return jsonify({"error": "Server API key not configured"}), 500

    key = request.headers.get("X-API-Key")
    if not key or key != data_api_key:
        return jsonify({"error": "Invalid or missing API key"}), 401

    return None


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------