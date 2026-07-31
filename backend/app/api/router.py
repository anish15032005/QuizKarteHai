from fastapi import APIRouter

# Import the route modules and reference their `router` attributes
from app.api.routes import health
from app.api.routes import user
from app.api.routes import auth

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(user.router)
api_router.include_router(auth.router)