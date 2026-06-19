from collections.abc import Generator

from fastapi import Depends
from fastapi import Header
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.user import User

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

def get_current_user(
    api_key: str = Header(alias="api-key"),
    db: Session = Depends(get_db),
) -> User:

    stmt = select(User).where(User.api_key == api_key)
    user = db.execute(stmt).scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid api key",
        )

    return user