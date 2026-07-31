from typing import cast

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token
from app.models.user import User
from app.schemas.user import UserLogin


def login_service(db: Session, user: UserLogin):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(
        user.password,
        cast(str, db_user.hashed_password),
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }