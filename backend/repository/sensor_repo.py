from sqlalchemy.orm  import Session
from backend.models.sensor import Sensor, SensorPrm
# from backend.schemas.sensor import SensorBase


def get_sensors(db:Session) -> list[Sensor]:
    print(db.query(Sensor).all())
    return list(db.query(Sensor).all())

def get_sensor(db:Session, sensor_id: int)->Sensor:
    return db.get(Sensor, sensor_id)