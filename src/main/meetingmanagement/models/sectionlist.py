from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class SectionList(Base):
    __tablename__ = 'sectionlist'
    id = Column("id",Integer, primary_key=True)
    listName = Column("listname",String, primary_key=True)
    sections = relationship("section",backref="sectionlist")

    meeting_id = Column("meeting_id",Integer, ForeignKey('meeting.id'))
    meeting = relationship("meeting",backref="sectionlist")


    def __init__(self, listName, sections,meeting_id):
        self.listName = listName
        self.sections = sections
        self.meeting_id = meeting_id
