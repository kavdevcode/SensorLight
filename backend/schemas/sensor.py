from pydantic import BaseModel, ConfigDict


class SensorBase(BaseModel):

    sensor_number: int 
    name: str
    id: int 
    
    
class SensorCreate(SensorBase):
    pass


class Sensor_list(SensorBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
