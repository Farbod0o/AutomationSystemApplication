from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class TimeShift(Base):
    __tablename__ = 'time_shift'

    _id = Column(Integer, primary_key=True)
    _start_time = Column(DateTime)
    _end_time = Column(DateTime)
    _total_hours = Column(Integer)

    administrative_calendar = relationship("AdministrativeCalendar", back_populates="time_shift")
    work_shift = relationship("WorkShift", back_populates="time_shift")
    leave = relationship("Leave", back_populates="time_shift")
    mission = relationship("Mission", back_populates="time_shift")

    def __init__(self, start_time, end_time, total_hours):
        self.start_time = start_time
        self.end_time = end_time
        self.total_hours = total_hours

