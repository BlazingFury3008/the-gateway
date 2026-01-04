import os
from flask import Blueprint, request, jsonify
from models import db, User, Character  # if unused, you can safely remove these

# Optional safety net: loads .env if python-dotenv is installed.
# This prevents "not configured" when the app doesn't auto-load env files.
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass


# ---------------------------------------------------------
# API Key auth
# ---------------------------------------------------------
def require_api_key():
    """Return (json, status) if unauthorized, otherwise None."""
    # Read env at call-time (not import-time)
    data_api_key = os.getenv("DATA_API_KEY")
    print("api")

    if not data_api_key:
        return jsonify({"error": "Server API key not configured"}), 500

    key = request.headers.get("X-API-Key")
    if not key or key != data_api_key:
        return jsonify({"error": "Invalid or missing API key"}), 401

    return None


# ---------------------------------------------------------
# Blueprint + config
# ---------------------------------------------------------
data_bp = Blueprint("data", __name__, url_prefix="/data")


@data_bp.before_request
def _check_api_key():
    # Let CORS preflight pass
    if request.method == "OPTIONS":
        return None

    #auth_error = require_api_key()
    #if auth_error:
    #    return auth_error
    #return None



from routes.V20 import v20_bp  

data_bp.register_blueprint(v20_bp)
