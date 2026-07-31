from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.database.database import Base, engine

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)