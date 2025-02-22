from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class WorkShift(Base):
    __tablename__ = 'work_shift'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    status = Column(Enum('active', 'inactive'))
    time_shift_id = Column(Integer, ForeignKey('time_shift.id'))

    time_shift = relationship('TimeShift', back_populates='work_shift')

    def __init__(self, name, status):
        self.name = name
        self.status = status

