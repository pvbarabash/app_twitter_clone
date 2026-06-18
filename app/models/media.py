from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.database import Base

class Media(Base):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    tweet_id: Mapped[int | None] = mapped_column(
        ForeignKey("tweets.id"),
        nullable=True
    )