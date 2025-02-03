from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class SectionList(Base):
    __tablename__ = 'sectionlist'
    listname = Column("listname",String, primary_key=True)
    sections = relationship("section",backref="sectionlist")

    def __init__(self, listname, sections):
        self.listname = listname
        self.sections = sections