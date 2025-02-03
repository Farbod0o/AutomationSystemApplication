from sqlalchemy import Column, Integer, String, Date, Time, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class MeetingStatus(enum.Enum):
    Scheduled = "Scheduled"
    Held = "Held"
    Canceled = "Canceled"

class Meeting(Base):
    __tablename__ = 'meeting'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    day_of_week = Column(String(20), nullable=False)
    location = Column(String(100), nullable=False)
    meeting_manager = Column(String(50), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    title = Column(String(100), nullable=False)
    status = Column(Enum(MeetingStatus), nullable=False)
    description = Column(String(255), nullable=True)

    def __init__(self, date, day_of_week, location, meeting_manager, start_time, end_time, title, status, description=""):
        self.date = date
        self.day_of_week = day_of_week
        self.location = location
        self.meeting_manager = meeting_manager
        self.start_time = start_time
        self.end_time = end_time
        self.title = title
        self.status = status
        self.description = description

    def __str__(self):
        return f"Meeting (Title: {self.title}, Date: {self.date}, Status: {self.status.value})"
