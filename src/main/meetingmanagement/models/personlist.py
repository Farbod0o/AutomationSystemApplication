from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class PersonList(Base):
    __tablename__ = 'personlist'
    id = Column("id",Integer, primary_key=True)
    listname = Column("listname",String(50), primary_key=True)

    minutesofmeeting_id =Column(Integer, ForeignKey('minutesofmeeting.id'))
    minutesofmeeting = relationship("MinutesOfMeeting")

    members = relationship("MemberList", backref="User")

    def __init__ (self, listname, members,minutesofmeeting_id):
        self.listname = listname
        self.members = members
        self.minutesofmeeting_id = minutesofmeeting_id