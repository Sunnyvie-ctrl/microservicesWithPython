import asyncio

import httpx

from fastapi import FastAPI, HTTPException

from app.database import SessionLocal
from app.schemas import ActivityCreate
from app import service

app = FastAPI(title="activity-service")


async def validate_user(user_id: str):
    retries = 3

    for attempt in range(retries):
        try:
            async with httpx.AsyncClient(
                timeout=5.0
            ) as client:

                response = await client.get(
                    f"http://localhost:8001/v1/users/{user_id}"
                )

            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail="User not found",
                )

            response.raise_for_status()

            return

        except httpx.RequestError:

            if attempt == retries - 1:
                raise HTTPException(
                    status_code=503,
                    detail="User service unavailable",
                )

            await asyncio.sleep(1)


async def fetch_game(game_id: str):

    try:
        async with httpx.AsyncClient(
            timeout=5.0
        ) as client:

            response = await client.get(
                f"http://localhost:8002/v1/games/{game_id}"
            )

        response.raise_for_status()

        return response.json()

    except Exception:
        return None


@app.post("/v1/activities")
async def create_activity(
    data: ActivityCreate,
):

    await validate_user(data.user_id)

    game = await fetch_game(data.game_id)

    db = SessionLocal()

    try:
        activity = service.add_activity(
            db,
            data,
            game,
        )

        return activity

    finally:
        db.close()