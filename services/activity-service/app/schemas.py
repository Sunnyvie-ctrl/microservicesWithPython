from pydantic import BaseModel


class ActivityCreate(BaseModel):
    user_id: str
    game_id: str
    action: str


class ActivityOut(BaseModel):
    id: str
    user_id: str
    game_id: str
    action: str
    game: dict | None = None

    model_config = {"from_attributes": True}


class ActivityList(BaseModel):
    items: list[ActivityOut]
    total: int
    limit: int
    offset: int