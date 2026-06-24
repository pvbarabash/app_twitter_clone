import shutil
import uuid
from pathlib import Path

from sqlalchemy.orm import Session

from app.models.media import Media

MEDIA_DIR = Path("media")
MEDIA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

class MediaService:

    @staticmethod
    def save_file(
        db: Session,
        uploaded_file,
    ) -> int:

        extension = (
            uploaded_file.filename
            .split(".")[-1]
        )

        filename = (
            f"{uuid.uuid4()}.{extension}"
        )

        filepath = (
            MEDIA_DIR / filename
        )

        with open(
            filepath,
            "wb",
        ) as buffer:
            shutil.copyfileobj(
                uploaded_file.file,
                buffer,
            )

        media = Media(
            file_path=str(filepath),
        )

        db.add(media)
        db.commit()
        db.refresh(media)

        return media.id