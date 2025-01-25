from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Mission(Base):
    __tablename__ = 'mission'
    id = Column(Integer, primary_key=True)
    extended_time = Column(DateTime)
    origin = Column(String(100))
    destination = Column(String(100))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    distance = Column(Integer)
    request_date = Column(DateTime)
    travel_method = Column(String(100))
    description = Column(String(300))
    accommodation = Column(String(300))

    time_sheet_id = Column(Integer, ForeignKey('time_sheet.id'))
    time_shift_id = Column(Integer, ForeignKey('time_shift.id'))

    time_sheet = relationship("TimeSheet", back_populates="mission")
    time_shift = relationship("TimeShift", back_populates="mission")

    def __init__(self, extended_time, origin, destination, start_date, end_date, distance, request_date, travel_method, description, accommodation):
        self.extended_time = extended_time
        self.origin = origin
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.distance = distance
        self.request_date = request_date
        self.travel_method = travel_method
        self.description = description
        self.accommodation = accommodation
