from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class AdministrativeCalendar(Base):
    __tablename__ = 'administrative_calendar'

    _id = Column(Integer, primary_key=True)
    _date = Column(DateTime)
    _start_time = Column(DateTime)
    _end_time = Column(DateTime)
    _day_of_week = Column(String(100))
    _is_holiday = Column(Boolean)

    _time_shift_id = Column(Integer, ForeignKey('time_shift.id'))
    _time_sheet_id = Column(Integer, ForeignKey('time_sheet.id'))

    time_shift = relationship('TimeShift', back_populates='administrative_calendar')
    time_sheet = relationship('TimeSheet', back_populates='administrative_calendar')

    def __init__(self, date, start_time, end_time, day_of_week, is_holiday):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.day_of_week = day_of_week
        self.is_holiday = is_holiday

