from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.repository import sensor_repo

def list_sensors(db:Session):
    print("---------------")
    return sensor_repo.get_sensors(db)

def sensor_by_id(db:Session, sensor_id):
    sensor = sensor_repo.get_sensor(db, sensor_id)
    if sensor is None:
        raise HTTPException(status_code=404, detail="not found")
    return sensor