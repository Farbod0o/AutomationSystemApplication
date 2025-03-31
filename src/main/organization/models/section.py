from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Section(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True, autoincrement=True)
    head = Column("Head", String(50))
    address = Column("Address", String(100))
    name = Column("Name", String(30))
    phoneNum = Column("Phone number", String(13))
    internalCode = Column("Internal code", String(10))
    description = Column("Description", String(100))
    sectionNum = Column("Section number", String(100))
    accessLevel = Column("Access level", String(100))
    higherLevelSectionNum = Column(String, nullable=True)

    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department")


    def __init__(self, id, head, address, name, phoneNum, internalCode, description, sectionNum,
                 accessLevel, higherLevelSectionNum, department_id):

        self.id = id
        self.head = head
        self.address = address
        self.name = name
        self.phoneNum = phoneNum
        self.internalCode= internalCode
        self.description = description
        self.sectionNum = sectionNum
        self.accessLevel = accessLevel
        self.higherLevelSectionNum = higherLevelSectionNum
        self.department_id = department_id
