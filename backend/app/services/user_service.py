from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def create_user_service(db: Session, user: UserCreate):
    new_user = User(
        name=user.name,
        email=user.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users_service(db: Session):
    return db.query(User).all()