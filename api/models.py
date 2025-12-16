from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime
import os
import uuid

db = SQLAlchemy()

PUBLIC_BASE_URL = os.getenv("FLASK_PUBLIC_BASE_URL", "http://localhost:5000")


# ---------------------------------------------------------
# Users
# ---------------------------------------------------------
class User(db.Model):
    __tablename__ = "users"

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
            "username": self.username,
            "image": image,
            "linked_accounts": self.linked_accounts or [],
            "created_at": self.created_at.isoformat(),
        }

# ---------------------------------------------------------
# Characters (your existing character data, fixed)
# ---------------------------------------------------------
class Character(db.Model):
    __tablename__ = "characters"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False,
    )

    name = db.Column(db.String(100), nullable=False)

    user_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id"),
        nullable=False,
    )
    user = db.relationship("User", backref="characters", lazy=True)

    data = db.Column(
        MutableList.as_mutable(JSON),
        default=list,
        nullable=False,
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "data": self.data,
            "created_at": self.created_at.isoformat(),
        }
