from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime
import os
import uuid

db = SQLAlchemy()
PUBLIC_BASE_URL = os.getenv("FLASK_PUBLIC_BASE_URL", "http://localhost:5000")


class User(db.Model):
    __tablename__ = "users"

    # UUID primary key as string
    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False,
    )

    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200))
    image = db.Column(db.String(255))

    # Important: MutableList so SQLAlchemy tracks list edits.
    linked_accounts = db.Column(
        MutableList.as_mutable(JSON),
        default=list,
        nullable=False,
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        image = self.image
        if image and image.startswith("/static/"):
            image = f"{PUBLIC_BASE_URL}{image}"

        return {
            "id": self.id,
            "email": self.email,
            "name": self.username,
            "image": image,
            "linked_accounts": self.linked_accounts or [],
        }
