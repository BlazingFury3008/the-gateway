from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from routes.auth import auth_bp
from routes.data import data_bp


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gateway.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "supersecretkey"

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # CORS: explicitly allow your Next.js dev origins + headers
    CORS(
        app,
        resources={
            r"/*": {
                "origins": [
                    "http://localhost:3000",
                    "http://192.168.1.140:3000",  # adjust if your Next URL differs
                ],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "X-API-Key", "Authorization"],
            }
        },
        supports_credentials=True,
    )

    # Register routes
    app.register_blueprint(auth_bp)
    app.register_blueprint(data_bp)

    @app.route("/")
    def index():
        return {"message": "Flask API running"}

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # creates the tables if they don't exist
        from seed.seed_v20 import seed_v20

        seed_v20()
    app.run(host="0.0.0.0", port=5000, debug=True)
