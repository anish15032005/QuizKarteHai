from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.auth.jwt_handler import create_access_token

from app.models.user import User
from app.schemas.user import UserLogin
from app.auth.hashing import verify_password


def login_user_service(db: Session, user: UserLogin):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(
        user.password,
        str(existing_user.password),
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
    {
        "sub": existing_user.email
    }
)

    return {
    "access_token": access_token,
    "token_type": "bearer",
}