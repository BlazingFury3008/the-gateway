from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema for user response
class UserResponse(BaseModel):
    uuid: str
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allows SQLAlchemy models to be returned as JSON

# Response Model for Authentication Tokens
class Token(BaseModel):
    access_token: str
    token_type: str
    user: Optional[UserResponse] = None