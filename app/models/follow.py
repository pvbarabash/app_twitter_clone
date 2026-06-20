from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


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

    follower = relationship(
        "User",
        foreign_keys=[follower_id],
        back_populates="following_relations",
    )

    following = relationship(
        "User",
        foreign_keys=[following_id],
        back_populates="follower_relations",
    )