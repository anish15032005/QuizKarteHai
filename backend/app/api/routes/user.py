from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate
from app.services.user_service import (
    create_user_service,
    get_users_service,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=list[UserResponse],
)
def get_users(db: Session = Depends(get_db)):
    return get_users_service(db)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201,
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)