import uuid
from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta
from database import get_mysql_db
from auth import hash_password, verify_password, create_access_token, decode_access_token
from schemas import UserCreate, UserResponse, Token, UserLogin

router = APIRouter(tags=["Users"])

### 🛠 SIGNUP (Register New User) ###
@router.post("/signup", response_model=Token)
def signup(user: UserCreate):
    """Registers a new user with a generated UUID"""
    try:
        with get_mysql_db() as (conn, cursor):
            # Check if user already exists
            cursor.execute("SELECT * FROM users WHERE email = %s", (user.email,))
            existing_user = cursor.fetchone()
            if existing_user:
                raise HTTPException(status_code=400, detail="Email already registered")

            # Generate a new UUID
            user_uuid = str(uuid.uuid4())

            # Hash password and insert new user
            hashed_pw = hash_password(user.password)
            cursor.execute(
                "INSERT INTO users (uuid, name, email, password) VALUES (%s, %s, %s, %s)", 
                (user_uuid, user.name, user.email, hashed_pw)
            )
            conn.commit()

            # Create access token
            access_token = create_access_token(data={"sub": user_uuid}, expires_delta=timedelta(minutes=30))
            return {"access_token": access_token, "token_type": "bearer", "uuid": user_uuid}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

### 🛠 LOGIN (Authenticate User) ###
@router.post("/login", response_model=Token)
def login(user: UserLogin):
    """Logs in a user and returns an access token"""
    try:
        with get_mysql_db() as (conn, cursor):
            # Find user by email
            cursor.execute("SELECT * FROM users WHERE email = %s", (user.email,))
            db_user = cursor.fetchone()

            if not db_user or not verify_password(user.password, db_user["password"]):
                raise HTTPException(status_code=401, detail="Invalid credentials")

            # Create access token
            access_token = create_access_token(data={"sub": db_user["uuid"]}, expires_delta=timedelta(minutes=30))

            return {
                "access_token": access_token,
                "token_type": "bearer",
                "user": {
                    "uuid": db_user["uuid"],
                    "name": db_user["name"],  
                    "email": db_user["email"],
                    "auth": db_user["auth"],
                },
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

### 🛠 GET CURRENT USER ###
@router.get("/users/me", response_model=UserResponse)
def get_current_user():
    """Validates if the user still exists using JWT token from headers."""
    try:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token format")

        token = authorization.split(" ")[1]
        user_data = decode_access_token(token)

        if not user_data:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = user_data.get("sub")

        with get_mysql_db() as (conn, cursor):
            cursor.execute("SELECT uuid, name, email FROM users WHERE uuid = %s", (user_id,))
            user = cursor.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

        return user

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching user: {str(e)}")