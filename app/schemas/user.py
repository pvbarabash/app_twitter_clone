from pydantic import BaseModel

class UserShortSchema(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

class UserProfileSchema(BaseModel):
    id: int
    name: str

    followers: list[UserShortSchema]
    following: list[UserShortSchema]

    model_config = {
        "from_attributes": True
    }


class UserResponseSchema(BaseModel):
    result: bool = True
    user: UserProfileSchema

