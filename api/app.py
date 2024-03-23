from fastapi import FastAPI

from api.routes.carros import carros_router
from api.lifespan import app_lifespan


app = FastAPI(
    lifespan=app_lifespan,
    redoc_url=None
)

app.include_router(carros_router)
