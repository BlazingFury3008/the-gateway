from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gateway.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "supersecretkey"

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app, supports_credentials=True)

    # Register routes
    app.register_blueprint(auth_bp)

    @app.route("/")
    def index():
        return {"message": "Flask API running"}

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # creates the tables if they don't exist
    app.run(host="0.0.0.0", port=5000, debug=True)
