from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="activity-service")

app.include_router(router)