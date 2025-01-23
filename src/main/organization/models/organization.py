from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base
from src.main.organization.models.associations import organization_permission_table


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True,autoincrement=True)
    manager = Column(String)
    address = Column(String)
    phoneNum=Column(String)
    logo = Column(String)
    task = Column(String)
    departmentNum = Column(String)
    description = Column(String)

    department = relationship('Department',secondary=organization_permission_table,back_populates='organization')

    def __init__(self,manager,address,phoneNum,logo,task,departmentNum,description=None):
        self.manager = manager
        self.address = address
        self.phoneNum = phoneNum
        self.logo = logo
        self.task = task
        self.departmentNum = departmentNum
        self.description = description




