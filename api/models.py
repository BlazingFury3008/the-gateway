from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import Enum
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
# Characters
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


# -----------------------------------------------
# V20 Data
# -----------------------------------------------
class V20_Clans(db.Model):
    __tablename__ = "v20_clans"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    weakness = db.Column(db.Text, nullable=False)
    information = db.Column(db.Text, nullable=False)
    reference = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "weakness": self.weakness,
            "information": self.information,
        }

class V20_Nature(db.Model):
    __tablename__ = "v20_nature"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.description,
        }

class V20_Backgrounds(db.Model):
    __tablename__ = "v20_backgrounds"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Use Integer here instead of db.Number
    increments = db.Column(db.Integer, default=1, nullable=False)
    max_value = db.Column(db.Integer, default=5, nullable=False)
    cost = db.Column(db.Integer, default=1, nullable=False)

    # Fix: Column, and probably you want Text or String
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "increments": self.increments,
            "maximum_value": self.max_value,
            "cost_mult": self.cost,
            "description": self.description,
        }

class V20_Merits(db.Model):
    __tablename__ = "v20_merits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cost = db.Column(db.Integer, default=1, nullable=False)
    type = db.Column(Enum("Physical", "Social", "Mental", "Supernatural", name="v20_flaw_enum"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "type": self.type,
        }
    
class V20_Flaws(db.Model):
    __tablename__ = "v20_flaws"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    severity = db.Column(db.Integer, default=1, nullable=False)
    type = db.Column(Enum("Physical", "Social", "Mental", "Supernatural", name="v20_flaw_enum"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.severity,
            "type": self.type,
        }
    
class V20_Disciplines(db.Model):
    __tablename__ = "v20_disciplines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
    
class V20_Discipline_Powers(db.Model):
    __tablename__ = "v20_discipline_powers"

    id = db.Column(db.Integer, primary_key=True)
    discipline_id = db.Column(db.Integer, db.ForeignKey("v20_disciplines.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    discipline = db.relationship("V20_Disciplines", backref="powers", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "discipline_id": self.discipline_id,
            "name": self.name,
            "level": self.level,
            "description": self.description,
        }

class V20_Magic_Types(db.Model):
    __tablename__ = "v20_magic_types"

    name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class V20_Sorcery_Paths(db.Model):
    __tablename__ = "v20_sorcery_paths"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    magic_type = db.Column(db.String(100), db.ForeignKey("v20_magic_types.name"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }