from fastapi import FastAPI
from api.routes.carros import carros_router


app = FastAPI()

app.include_router(carros_router)
