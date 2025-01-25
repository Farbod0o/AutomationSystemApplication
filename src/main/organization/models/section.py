from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Section:
    __tablename__ = 'sections'

    section_id = Column(Integer, primary_key=True, autoincrement=True)
    head = Column("Head", String(50))
    address = Column("Adress", String(100))
    name = Column("Name", String(30))
    phone_num = Column("Phone number", String(13))
    internal_code = Column("Internal code", String(10))
    description = Column("Description", String(100))
    section_num = Column("Section number", String(100))
    access_level = Column("Access level", String(100))
    higher_level_section_num = Column(String, nullable=True)

    employees = relationship('Employee', backref='section', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"<Section(name='{self.name}', head='{self.head}')>"

    def __init__(self, section_id, head, address, name, phone_num, internal_code, description, section_num,
                 access_level, higher_level_section_num):
        # Constructor of the Section class that initializes the section information
        self.section_id = section_id
        self.head = head
        self.address = address
        self.name = name
        self.phone_num = phone_num
        self.internal_code = internal_code
        self.description = description
        self.section_num = section_num
        self.access_level = access_level
        self.higher_level_section_num = higher_level_section_num
        self.employees = []  # Initializing the list of employees
