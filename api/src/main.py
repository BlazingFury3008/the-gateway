from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import metadata, engine
import threading
import time
from routers.api_keys import router as api_keys_router
from routers.routers import router as dynamic_router
from routers.all_data import router as all_data_router
from routers.user_auth import router as user_auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://192.168.1.139:3000"],  # Add specific origins instead of "*"
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Excluded tables that should not be exposed via API
EXCLUDED_TABLES = {"users", "admin_logs"}

# Function to dynamically rebuild API routes when a new table is added
def rebuild_routes():
    global metadata
    print("🔄 Rebuilding API routes...")

    with engine.connect() as conn:
        metadata.reflect(bind=conn)  # Reflect updated database schema

    active_routes = set()

    for table_name, table in metadata.tables.items():
        if table_name in EXCLUDED_TABLES or table_name in active_routes:
            continue

        print(f"📌 Registering API routes for: {table_name}")
        active_routes.add(table_name)

    print("✅ Route rebuild complete!")

# Register static API key routes
app.include_router(api_keys_router)

# Register dynamic API routes
app.include_router(dynamic_router)

# Register table get router 
app.include_router(all_data_router)

# Register user auth route
app.include_router(user_auth_router)

# Run an initial rebuild to load existing tables
rebuild_routes()
