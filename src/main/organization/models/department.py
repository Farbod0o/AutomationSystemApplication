from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base
from src.main.organization.models.associations import organization_permission_table


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    manager = Column("manager",String(100))
    address = Column("address",String(100))
    name = Column("name",String(100))
    phoneNum = Column("phoneNum",String(100))
    logo = Column("log",String(100))
    description = Column("description",String(100))
    departmentNum= Column("departmentNum",String(100))
    task = Column("task",String(100))

    organization = relationship('Organization',secondary=organization_permission_table,back_populates='departments')

    def __init__(self,manager,address,name,phoneNum,logo,description,departmentNum,task):
        self.manager = manager
        self.address = address
        self.name = name
        self.phoneNum = phoneNum
        self.logo = logo
        self.description = description
        self.departmentNum = departmentNum
        self.task = task

