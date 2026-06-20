from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    api_key: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    follower_relations = relationship(
        "Follow",
        foreign_keys="Follow.following_id",
        back_populates="following",
        cascade="all, delete-orphan",
    )

    following_relations = relationship(
        "Follow",
        foreign_keys="Follow.follower_id",
        back_populates="follower",
        cascade="all, delete-orphan",
    )