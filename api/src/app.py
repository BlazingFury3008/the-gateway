from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users

app = FastAPI()

origins = [
    "http://localhost:3000",  # Frontend running on Next.js (development)
    "http://localhost:3001",  # Frontend running on Next.js (development)
    "https://yourdomain.com", # Production domain
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(users.router)

@app.get("/")
def index():
    return {"message": "Hello Worlds"}
