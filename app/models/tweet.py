from datetime import datetime, timezone

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base

class Tweet(Base):
    __tablename__ = "tweets"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    content: Mapped[str] = mapped_column(
        String(280),
        nullable=False
    )

    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc)

    )