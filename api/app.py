from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flasgger import Swagger

from models import db
from routes.auth import auth_bp
from routes.data import data_bp


def create_app():
    app = Flask(__name__)

    # -------------------------------------------------
    # Core config
    # -------------------------------------------------
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gateway.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "supersecretkey"

    # -------------------------------------------------
    # Extensions
    # -------------------------------------------------
    db.init_app(app)
    Migrate(app, db)

    CORS(
        app,
        resources={
            r"/*": {
                "origins": [
                    "http://localhost:3000",
                    "http://192.168.1.140:3000",
                ]
            }
        },
        supports_credentials=True,
    )

    # -------------------------------------------------
    # Swagger / Flasgger
    # -------------------------------------------------
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Gateway API",
            "description": "Flask API with Swagger docs",
            "version": "1.0.0",
        },
        "security": [{"ApiKeyAuth": []}],
        "definitions": {
            "V20_Discipline": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "example": 3},
                    "name": {"type": "string", "example": "Potence"},
                    "description": {
                        "type": "string",
                        "example": "Supernatural strength",
                    },
                },
            },
            "V20_Clan": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "weakness": {"type": "string"},
                    "information": {"type": "string"},
                    "reference": {"type": "string"},
                    "discipline_1": {"$ref": "#/definitions/V20_Discipline"},
                    "discipline_2": {"$ref": "#/definitions/V20_Discipline"},
                    "discipline_3": {"$ref": "#/definitions/V20_Discipline"},
                    "discipline_4": {"$ref": "#/definitions/V20_Discipline"},
                },
            },
            "V20_Background": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "increments": {"type": "integer"},
                    "maximum_value": {"type": "integer"},
                    "cost_mult": {"type": "integer"},
                    "description": {"type": "string"},
                },
            },
            "V20_Nature": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                },
            },
            "V20_Path_Power": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {
                        "type": "string",
                    },
                    "system": {
                        "type": "string",
                    },
                },
            },
            "V20_Sorcery_Path": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "reference": {"type": "string"},
                    "powers": {
                        "type": "array",
                        "properties": {"$ref": "#/definitions/V20_Path_Power"},
                    },
                },
            },
            "V20_Advantage": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "rating": {"type": "integer"},
                    "description": {"type": "string"},
                    "reference": {"type": "string"},
                },
            },
        },
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Use: Bearer <token>",
            },
            "ApiKeyAuth": {
                "type": "apiKey",
                "name": "X-API-Key",
                "in": "header",
            },
        },
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs",
        "uiversion": 3,
    }

    Swagger(app, template=swagger_template, config=swagger_config)

    # -------------------------------------------------
    # Blueprints
    # -------------------------------------------------
    app.register_blueprint(auth_bp)
    app.register_blueprint(data_bp)

    # -------------------------------------------------
    # Root
    # -------------------------------------------------
    @app.get("/")
    def index():
        return {"message": "Flask API running"}

    return app


# -----------------------------------------------------
# Entrypoint
# -----------------------------------------------------
if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()
        from seed.seed_v20 import seed_v20

        seed_v20()

    app.run(host="0.0.0.0", port=5000, debug=True)
