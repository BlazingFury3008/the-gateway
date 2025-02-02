from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(users.router)

@app.get("/")
def index():
    return {"message": "Hello Worlds"}
