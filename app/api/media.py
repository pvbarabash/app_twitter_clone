from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user,
)

from app.models.user import User

from app.schemas.media import (
    MediaUploadResponseSchema,
)

from app.services.media_service import (
    MediaService,
)

router = APIRouter(
    prefix="/api/medias",
    tags=["Media"],
)

@router.post(
    "",
    response_model=MediaUploadResponseSchema,
)
def upload_media(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    media_id = (
        MediaService.save_file(
            db=db,
            uploaded_file=file,
        )
    )

    return {
        "result": True,
        "media_id": media_id,
    }