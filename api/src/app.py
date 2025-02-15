from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, data

app = FastAPI(
    title="The Gateway API",
    description="API for The Gateway website",
    version="1.0.0",
    openapi_tags=[
        {"name": "Users", "description": "User related operations"},
        {"name": "Database", "description": "Database management operations"},
    ]
)

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://yourdomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(users.router)
app.include_router(data.router)

@app.get("/")
def index():
    return {"message": "Hello Worlds"}
