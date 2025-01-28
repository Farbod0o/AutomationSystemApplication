from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table

class Chat(Base):
    __tablename__ = "chat_tbl"

    _chat_id = Column(Integer, primary_key=True, autoincrement=True)
    _participantOne = Column("participantOne", String(30))
    _participantTwo = Column("participantTwo", String(30))
    _creationDate = Column("creationDate", DateTime)

    notification = relationship("Notification", uselist=False, back_populates="notification_tbl")
    attachment = relationship("Attachment",  uselist=False, back_populates="chat_tbl")
    message = relationship("Message", back_populates="chat_tbl")

    statusupdate_id = Column(Integer, ForeignKey("statusupdate_id"))
    statusupdate = relationship("StatusUpdate", back_populates="chat_tbl")

    def __init__(self, participant_one, participant_two, creation_date=None):
        self._participantOne = participant_one
        self._participantTwo = participant_two
        self.creation_date = creation_date if creation_date is not None else DateTime.now()


def __repr__(self):
    return f"<Notification(id={self.id}, participant_one='{self.participant_one}', " \
           f"participant_two='{self.participent_two}', creation_date='{self.creation_date}')>"
