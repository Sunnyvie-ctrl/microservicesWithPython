from sqlalchemy.orm import Session

from app import repository
from app.schemas import (
    ActivityCreate,
    ActivityOut,
    ActivityList,
)


def add_activity(
    db: Session,
    data: ActivityCreate,
    game: dict | None = None,
):

    activity = repository.create_activity(
        db,
        data,
    )

    result = ActivityOut.model_validate(activity)
    result.game = game

    return result


def fetch_all_activities(
    db: Session,
    limit: int = 20,
    offset: int = 0,
):

    activities, total = repository.list_activities(
        db,
        limit,
        offset,
    )

    return ActivityList(
        items=[
            ActivityOut.model_validate(a)
            for a in activities
        ],
        total=total,
        limit=limit,
        offset=offset,
    )