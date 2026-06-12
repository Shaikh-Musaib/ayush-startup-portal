from fastapi import FastAPI
from app.db.database import engine, Base
import app.models

# Import Routers
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router


app = FastAPI(
    title="AYUSH Startup Portal API",
    description="""
    AYUSH Startup Portal Backend API

    Features:
    - User Registration
    - User Login
    - JWT Authentication
    - User Profile Management
    - Startup Registration (Upcoming)
    - Admin Dashboard (Upcoming)
    """,
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    print("\n===== Creating Database Tables =====")

    Base.metadata.create_all(bind=engine)

    print("Tables detected by SQLAlchemy:")
    print(list(Base.metadata.tables.keys()))

    print("===== Startup Complete =====\n")


app.include_router(auth_router)
app.include_router(profile_router)


@app.get("/", tags=["Home"])
def root():
    return {
        "message": "Welcome to AYUSH Startup Portal API",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "database": "connected"
    }