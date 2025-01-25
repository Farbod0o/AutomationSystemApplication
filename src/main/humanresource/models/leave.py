from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Leave(Base):
    __tablename__ = 'leave'

    id = Column(Integer, primary_key=True)
    leave_type = Column(String(100))
    end_time = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(Enum("Pending", "Approved", "Rejected"))
    registration_date = Column(DateTime)
    description = Column(String(250))
    time_shift_id = Column(Integer, ForeignKey('time_shift.id'))
    time_sheet_id = Column(Integer, ForeignKey('time_sheet.id'))

    time_shift = relationship("TimeShift", back_populates="leave")
    time_sheet = relationship("TimeSheet", back_populates="leave")

    def __init__(self, leave_type, end_time, start_date, end_date, status, registration_date, description):
        self.leave_type = leave_type
        self.end_time = end_time
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.registration_date = registration_date
        self.description = description

