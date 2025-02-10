from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from database import get_db
from models import User
from auth import hash_password, verify_password, create_access_token
from schemas import UserCreate, UserResponse, Token, UserLogin

router = APIRouter()

@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.uuid}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.uuid}, expires_delta=timedelta(minutes=30))

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "uuid": db_user.uuid,
            "name": db_user.name,  
            "email": db_user.email,
        },
    }

