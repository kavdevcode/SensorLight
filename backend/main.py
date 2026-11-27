from fastapi import FastAPI

from backend.config import settings
from backend.database import engine, Base
from backend.models.sensor import Sensor, SensorPrm
from backend.routers import sensor


Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.app_name)
app.include_router(sensor.router)

@app.get("/")
def root():
    return {"app": settings.app_name, "status": "ok"}
