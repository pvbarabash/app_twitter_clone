from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base

class Follow(Base):
    __tablename__ = "follows"

    follower_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )

    following_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )