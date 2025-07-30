import jwt
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db
from auth_utils import create_jwt_token, verify_password, hash_password, verify_jwt_token
from models import User
from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime

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
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_jwt_token({"sub": user.uuid})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "uuid": user.uuid,
            "name": user.username,
            "email": user.email,
            "auth": user.auth_level,
            "config": user.config
        },
    }

@router.post("/signup")
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == request.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered.")

        hashed_password = hash_password(request.password)
        new_user = User(
            uuid=str(uuid.uuid4()),
            email=request.email,
            username=request.username,
            hashed_password=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token = create_jwt_token({"sub": new_user.uuid})
        return {"id": new_user.uuid, "email": new_user.email, "access_token": token}

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/refresh-token")
async def refresh_token(request: Request, db: Session = Depends(get_db)):
    """Refresh the access token if it's still valid."""
    try:
        body = await request.json()
        old_token = body.get("accessToken")

        if not old_token:
            raise HTTPException(status_code=400, detail="No access token provided")

        try:
            payload = verify_jwt_token(old_token)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired, login required")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: No user ID found")

        user = db.query(User).filter(User.uuid == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        exp_timestamp = payload.get("exp", 0)
        current_timestamp = datetime.utcnow().timestamp()
        if current_timestamp > exp_timestamp:
            raise HTTPException(status_code=401, detail="Token expired, login required")

        new_token = create_jwt_token({"sub": user.uuid})
        return {"access_token": new_token}

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/google-auth")
async def google_auth(request: Request, db: Session = Depends(get_db)):
    """
    Handles Google OAuth user verification and provisioning.
    1. Check if email exists:
        - If yes and account connected → login
        - If yes and account NOT connected → refuse login
        - If no → create account and return user
    """
    body = await request.json()
    account = body.get("account")
    profile = body.get("profile")
    email = profile.get("email") if profile else None
    google_id = account.get("providerAccountId") if account else None

    if not account or account.get("provider") != "google":
        raise HTTPException(status_code=400, detail="Invalid account provider")
    if not email or not google_id:
        raise HTTPException(status_code=400, detail="Missing Google account data")

    user = db.query(User).filter(User.email == email).first()

    if user:
        if user.google_id == google_id:
            token = create_jwt_token({"sub": user.uuid})
            return {"access_token": token, "user": {"uuid": user.uuid, "name": user.username, "email": user.email}}
        else:
            raise HTTPException(status_code=400, detail="Email already registered with a different login method")
    else:
        new_user = User(
            uuid=str(uuid.uuid4()),
            email=email,
            username=profile.get("name", email.split("@")[0]),
            google_id=google_id
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token = create_jwt_token({"sub": new_user.uuid})
        return {"access_token": token, "user": {"uuid": new_user.uuid, "name": new_user.username, "email": new_user.email}}

@router.post("/discord-auth")
async def discord_auth(request: Request, db: Session = Depends(get_db)):
    """
    Handles Discord OAuth user verification and provisioning.
    1. Check if email exists:
        - If yes and account connected → login
        - If yes and account NOT connected → refuse login
        - If no → create account and return user
    """
    body = await request.json()
    account = body.get("account")
    profile = body.get("profile")
    email = profile.get("email") if profile else None
    discord_id = account.get("providerAccountId") if account else None

    if not account or account.get("provider") != "discord":
        raise HTTPException(status_code=400, detail="Invalid account provider")
    if not email or not discord_id:
        raise HTTPException(status_code=400, detail="Missing Discord account data")

    user = db.query(User).filter(User.email == email).first()

    if user:
        if user.discord_id == discord_id:
            token = create_jwt_token({"sub": user.uuid})
            return {"access_token": token, "user": {"uuid": user.uuid, "name": user.username, "email": user.email}}
        else:
            raise HTTPException(status_code=400, detail="Email already registered with a different login method")
    else:
        new_user = User(
            uuid=str(uuid.uuid4()),
            email=email,
            username=profile.get("username", email.split("@")[0]),
            discord_id=discord_id
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token = create_jwt_token({"sub": new_user.uuid})
        return {"access_token": token, "user": {"uuid": new_user.uuid, "name": new_user.username, "email": new_user.email}}
