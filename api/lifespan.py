from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.logger import configure_logger


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    configure_logger()
    yield
