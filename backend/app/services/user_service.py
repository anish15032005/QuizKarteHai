from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.auth.hashing import hash_password

from app.models.user import User
from app.schemas.user import UserCreate


def create_user_service(db: Session, user: UserCreate):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered.",
        )

    new_user = User(
    name=user.name,
    email=user.email,
    hashed_password=hash_password(user.password),
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users_service(db: Session):
    return db.query(User).all()