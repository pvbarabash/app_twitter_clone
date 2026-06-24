from pydantic import BaseModel

class MediaUploadResponseSchema(BaseModel):
    result: bool = True
    media_id: int

class MediaSchema(BaseModel):
    id: int
    file_path: str

    model_config = {
        "from_attributes": True
    }