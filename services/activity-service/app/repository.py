from sqlalchemy.orm import Session

from app.models import Activity
from app.schemas import ActivityCreate


def create_activity(
    db: Session,
    data: ActivityCreate,
):

    activity = Activity(
        user_id=data.user_id,
        game_id=data.game_id,
        action=data.action,
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity


def list_activities(
    db: Session,
    limit: int = 20,
    offset: int = 0,
):

    total = db.query(Activity).count()

    activities = (
        db.query(Activity)
        .offset(offset)
        .limit(limit)
        .all()
    )

    return activities, total