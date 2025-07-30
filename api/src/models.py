import uuid
from sqlalchemy import Column, String, Boolean, Integer, JSON
from database import Base

class APIKey(Base):
    __tablename__ = "api_keys"

    api_key = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), unique=True, nullable=False)  # Identify the key owner or purpose
    is_active = Column(Boolean, default=True)  # Allow disabling keys

class User(Base):
    __tablename__ = "users"

    uuid = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=True)  # Nullable to support OAuth-only users
    google_id = Column(String(255), unique=True, nullable=True)
    discord_id = Column(String(255), unique=True, nullable=True)
    auth_level = Column(Integer, default=1)
    config = Column(JSON, default={})  # Store user configuration as JSON
