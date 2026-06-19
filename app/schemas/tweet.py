from pydantic import BaseModel
from app.schemas.media import MediaSchema


class TweetCreateSchema(BaseModel):
    tweet_data: str
    tweet_media_ids: list[int] = []

class TweetAuthorSchema(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

class LikeUserSchema(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

class TweetSchema(BaseModel):
    id: int
    content: str

    author: TweetAuthorSchema

    attachments: list[MediaSchema]

    likes: list[LikeUserSchema]

    model_config = {
        "from_attributes": True
    }

class FeedResponseSchema(BaseModel):
    result: bool = True
    tweets: list[TweetSchema]

class TweetCreateResponse(BaseModel):
    result: bool = True
    tweet_id: int