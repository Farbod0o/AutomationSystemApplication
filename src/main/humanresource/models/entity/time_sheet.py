from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class TimeSheet(Base):
    __tablename__ = 'time_sheet'

    _id = Column(Integer, primary_key=True)
    _entry_time = Column(DateTime)
    _exit_time = Column(DateTime)
    _date = Column(DateTime)
    _day_of_week = Column(String(100))
    _is_absent = Column(Boolean, default=False)
    _absence_description = Column(String(300))

    administrative_calendar = relationship('AdministrativeCalendar', back_populates='time_sheet')
    leave = relationship('Leave', back_populates='time_sheet')
    mission = relationship('Mission', back_populates='time_sheet')

    def __init__(self, entry_time, exit_time, date, day_of_week, is_absent, absence_description):
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.date = date
        self.day_of_week = day_of_week
        self.is_absent = is_absent
        self.absence_description = absence_description

_