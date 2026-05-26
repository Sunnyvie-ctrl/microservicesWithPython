from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app import service, schemas

router = APIRouter(
    prefix="/v1/activities",
    tags=["activities"],
)


@router.post(
    "/",
    response_model=schemas.ActivityOut,
    status_code=201,
)
def create_activity(
    data: schemas.ActivityCreate,
    db: Session = Depends(get_db),
):

    return service.add_activity(
        db,
        data,
    )


@router.get(
    "/",
    response_model=schemas.ActivityList,
)
def list_activities(
    limit: int = 20,
    offset: int = 0,
    db: Session = Depends(get_db),
):

    return service.fetch_all_activities(
        db,
        limit,
        offset,
    )