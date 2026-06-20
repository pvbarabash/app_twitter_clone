from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.follow import Follow
from app.models.user import User

class FollowService:

    @staticmethod
    def follow_user(
        db: Session,
        follower_id: int,
        following_id: int,
    ) -> None:

        # нельзя подписаться на себя
        if follower_id == following_id:
            raise ValueError(
                "Cannot follow yourself"
            )

        # существует ли пользователь
        user = db.get(
            User,
            following_id,
        )

        if user is None:
            raise ValueError(
                "User not found"
            )

        # есть ли уже подписка
        stmt = select(Follow).where(
            Follow.follower_id == follower_id,
            Follow.following_id == following_id,
        )

        existing_follow = (
            db.execute(stmt)
            .scalar_one_or_none()
        )

        if existing_follow:
            raise ValueError(
                "Already following"
            )

        follow = Follow(
            follower_id=follower_id,
            following_id=following_id,
        )

        db.add(follow)
        db.commit()

    @staticmethod
    def unfollow_user(
            db: Session,
            follower_id: int,
            following_id: int,
    ) -> None:

        stmt = select(Follow).where(
            Follow.follower_id == follower_id,
            Follow.following_id == following_id,
        )

        follow = (
            db.execute(stmt)
            .scalar_one_or_none()
        )

        if follow is None:
            raise ValueError(
                "Follow not found"
            )

        db.delete(follow)
        db.commit()