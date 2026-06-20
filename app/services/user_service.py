from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.user import User

class UserService:

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int,
    ) -> User | None:

        stmt = (
            select(User)
            .where(User.id == user_id)
        )

        return (
            db.execute(stmt)
            .scalar_one_or_none()
        )

    @staticmethod
    def get_profile(
            db: Session,
            user_id: int,
    ) -> dict | None:
        user = UserService.get_by_id(
            db=db,
            user_id=user_id,
        )

        if user is None:
            return None

        followers = [
            {
                "id": relation.follower.id,
                "name": relation.follower.name,
            }
            for relation in user.follower_relations
        ]

        following = [
            {
                "id": relation.following.id,
                "name": relation.following.name,
            }
            for relation in user.following_relations
        ]

        return {
            "id": user.id,
            "name": user.name,
            "followers": followers,
            "following": following,
        }
