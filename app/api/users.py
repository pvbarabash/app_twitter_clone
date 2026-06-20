from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.user import UserResponseSchema
from app.services.user_service import UserService
from app.services.follow_service import FollowService

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
)

@router.get(
    "/me",
    response_model=UserResponseSchema,
)
def get_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = UserService.get_profile(
        db=db,
        user_id=current_user.id,
    )

    return {
        "result": True,
        "user": profile,
    }

@router.get(
    "/{user_id}",
    response_model=UserResponseSchema,
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    profile = UserService.get_profile(
        db=db,
        user_id=user_id,
    )

    return {
        "result": True,
        "user": profile,
    }

@router.post("/{user_id}/follow")
def follow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user,
    ),
):

    try:
        FollowService.follow_user(
            db=db,
            follower_id=current_user.id,
            following_id=user_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    return {
        "result": True,
    }

@router.delete("/{user_id}/follow")
def unfollow_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user,
    ),
):

    try:
        FollowService.unfollow_user(
            db=db,
            follower_id=current_user.id,
            following_id=user_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )

    return {
        "result": True,
    }
