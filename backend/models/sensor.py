from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_number: Mapped[int] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    sensor_prm: Mapped[list["SensorPrm"]] = relationship(
        back_populates="sensor")


class SensorPrm(Base):
    __tablename__ = "sensors_prm"

    id: Mapped[int] = mapped_column(primary_key=True)
    sensor_id: Mapped[int] = mapped_column(ForeignKey(
        "sensors.id", ondelete="CASCADE"), nullable=False)
    tag: Mapped[str] = mapped_column(String(5), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    unit: Mapped[str | None] = mapped_column(String(10), nullable=False)

    sensor: Mapped["Sensor"] = relationship(back_populates="sensor_prm")
