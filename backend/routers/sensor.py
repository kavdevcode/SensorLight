from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.services import sensor_svr
from backend.schemas.sensor import SensorBase

router = APIRouter(prefix="/sensor", tags=["sensor"])


@router.get("/", response_model=list[SensorBase])
def list_sensors(db: Session = Depends(get_db)):
    return sensor_svr.list_sensors(db)

@router.get("/{sensor_id}", response_model=SensorBase)
def sensor_id(sensor_id:int, db: Session = Depends(get_db)):
    return sensor_svr.sensor_by_id(db, sensor_id)