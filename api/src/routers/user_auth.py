from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth_utils import create_jwt_token, verify_password, hash_password
from models import User
from pydantic import BaseModel, EmailStr
import uuid

router = APIRouter()

# Login request model
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    
# Signup request model
class SignupRequest(BaseModel):
    email: EmailStr
    username: str
    password: str

@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == request.email).first()
        if not user or not verify_password(request.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        # Generate JWT token
        token = create_jwt_token({"sub": user.uuid})

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "id": user.uuid,  # Ensure UUID is returned
                "name": user.username,  # Ensure the frontend expects "name"
                "email": user.email,
                "auth": user.auth_level,  # Ensure auth level is returned
            },
        }

    except Exception as e:
        print(f"🚨 Login Error: {str(e)}")  # Debugging in terminal
        raise HTTPException(status_code=500, detail="Internal Server Error")



@router.post("/signup")
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == request.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered.")

        # Hash password and create user with explicit UUID
        hashed_password = hash_password(request.password)
        new_user = User(
            uuid=str(uuid.uuid4()),  # Ensure UUID is assigned
            email=request.email,
            username=request.username,
            hashed_password=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Generate JWT token
        token = create_jwt_token({"sub": new_user.uuid})

        return {"id": new_user.uuid, "email": new_user.email, "access_token": token}

    except Exception as e:
        db.rollback()  # Prevent partial user creation
        print(f"🚨 Signup Error: {str(e)}")  # Debugging
        raise HTTPException(status_code=500, detail="Internal Server Error")
