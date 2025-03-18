from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt
import datetime
import bcrypt

from database import get_db
from models import APIKey
from config import SECRET_KEY


API_KEY_HEADER = APIKeyHeader(name="X-API-KEY", auto_error=True)

def validate_api_key(api_key: str = Security(API_KEY_HEADER), db: Session = Depends(get_db)):
    """
    Validates the API key provided in the request header.
    """
    key = db.query(APIKey).filter_by(api_key=api_key, is_active=True).first()

    if not key:
        raise HTTPException(
            status_code=403,
            detail="Invalid or inactive API key. Ensure you have the correct key and that it is active."
        )
    
    return key

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Function to create JWT token
def create_jwt_token(data: dict, expires_delta: int = 60*48):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

# Function to verify JWT token
def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Function to hash passwords
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Function to verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())