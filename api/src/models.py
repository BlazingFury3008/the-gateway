import uuid
from sqlalchemy import Column, String, Boolean, Integer
from database import Base

class APIKey(Base):
    __tablename__ = "api_keys"

    api_key = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)  # To identify the key owner or purpose
    is_active = Column(Boolean, default=True)  # Allow disabling keys

class User(Base):
    __tablename__ = "users"

    uuid = Column(String(255), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    username = Column(String(255), unique=False, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    auth_level = Column(Integer, default=1)
