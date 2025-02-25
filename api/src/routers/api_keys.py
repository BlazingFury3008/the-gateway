from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import get_db
from models import APIKey
import uuid
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
ADMIN_SECRET_KEY = os.getenv("ADMIN_SECRET_KEY")  # Secret key for admin actions

router = APIRouter()

# Dependency to check secret key authorization
def verify_admin_secret(secret_key: str = Header(None)):
    if secret_key != ADMIN_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing secret key.")

@router.post("/generate-api-key/", tags=["API_Keys"], dependencies=[Depends(verify_admin_secret)])
def generate_api_key(name: str, db: Session = Depends(get_db)):
    """
    Generates a new API key. Requires the admin secret key.
    """
    # Check if name already exists
    existing_key = db.query(APIKey).filter(APIKey.name == name).first()
    if existing_key:
        raise HTTPException(status_code=400, detail="API Key with this name already exists.")

    new_key = APIKey(api_key=str(uuid.uuid4()), name=name, is_active=True)
    db.add(new_key)
    db.commit()
    db.refresh(new_key)
    return {"message": "API Key created", "api_key": new_key.api_key}

@router.get("/list-api-keys/", tags=["API_Keys"], dependencies=[Depends(verify_admin_secret)])
def list_api_keys(db: Session = Depends(get_db)):
    """
    Lists all API keys (Admin use). Requires the admin secret key.
    """
    return db.query(APIKey).all()

@router.post("/disable-api-key/", tags=["API_Keys"], dependencies=[Depends(verify_admin_secret)])
def disable_api_key(api_key: str, db: Session = Depends(get_db)):
    """
    Disables an API key. Requires the admin secret key.
    """
    key = db.query(APIKey).filter(APIKey.key == api_key).first()
    if not key:
        raise HTTPException(status_code=404, detail="API Key not found.")
    
    key.is_active = False
    db.commit()
    return {"message": "API Key disabled"}

@router.post("/enable-api-key/", tags=["API_Keys"], dependencies=[Depends(verify_admin_secret)])
def enable_api_key(api_key: str, db: Session = Depends(get_db)):
    """
    Enables an API key. Requires the admin secret key.
    """
    key = db.query(APIKey).filter(APIKey.key == api_key).first()
    if not key:
        raise HTTPException(status_code=404, detail="API Key not found.")
    
    key.is_active = True
    db.commit()
    return {"message": "API Key enabled"}
