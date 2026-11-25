

from config import settings
from models.sensor import Sensor, SensorPrm
from database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)


def create_sensor():

    db = SessionLocal()
    try:
        s = Sensor(sensor_number=4, name="Sensor4",
                   sensor_prm=[
                       SensorPrm(tag="temp", name="temperature", unit="t")]

                   )

        db.add(s)
        db.commit()
        db.flush()
        print("ddd")
    finally:
        db.close()


def add_param(sensor_id):
    db = SessionLocal()
    sensor = db.get(Sensor, sensor_id)
    if sensor is None:
        raise ValueError("not found")

    sensor.sensor_prm.append(
        SensorPrm(tag="Pres3", name="pressure3", unit="P3"))
    db.commit()


def get_sensor():
    db = SessionLocal()
    sensor = db.get(Sensor, 2)
    if sensor is None:
        raise ValueError("not found")

    for n in sensor.sensor_prm:
        print(f"сенсор ={sensor.name} параметры={n.tag}")


get_sensor()
# create_sensor()
# add_param(1)
