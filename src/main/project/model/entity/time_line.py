from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base


class TimeLine(Base):
    __tablename__ = "time_lines"

    time_line_id = Column("report_ID", Integer, primary_key=True, autoincrement=True)
    start_date = Column("start_date", DateTime, nullable=False)
    end_date = Column("end_date", DateTime, nullable=False)
    description = Column("description", String(100), nullable=False)
    duration = Column("duration", String(30), nullable=False) # Question ??????
    registration_date = Column("registration_date", DateTime, nullable=False)

    ### relaitions to do

    def __init__(self, time_line_id, start_date, end_date, description, duration, registration_date):
        self.time_line_id = time_line_id
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.duration = duration
        self.registration_date = registration_date
        

