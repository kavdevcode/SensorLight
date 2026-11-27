from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.repository import sensor_repo

def list_sensors(db:Session):
    print("---------------")
    return sensor_repo.get_sensors(db)