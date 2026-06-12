from fastapi import FastAPI
from app.db.database import engine, Base
import app.models

from app.api.auth import router as auth_router


app = FastAPI(
    title="AYUSH Startup Portal API",
    description="Backend API for AYUSH Startup Portal",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# Register Authentication Routes
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AYUSH Startup Portal API",
        "status": "running"
    }