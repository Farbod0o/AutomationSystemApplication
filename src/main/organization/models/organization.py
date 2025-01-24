from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True, autoincrement=True)
    manager = Column(String(50))
    address = Column(String(100))
    phoneNum = Column(String(50))
    logo = Column(String(50))
    task = Column(String(50))
    departmentNum = Column(String(50))
    description = Column(String(100))

    departments = relationship('Department', back_populates='organization')

    def __init__(self, manager, address, phoneNum, logo, task, departmentNum, description=None):
        self.manager = manager
        self.address = address
        self.phoneNum = phoneNum
        self.logo = logo
        self.task = task
        self.departmentNum = departmentNum
        self.description = description
