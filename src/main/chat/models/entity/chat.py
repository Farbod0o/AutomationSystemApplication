from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.User import User


class Chat(Base):
    __tablename__ = "Chat_tbl"

    chat_id = Column("chat_ID", Integer, primary_key=True, autoincrement=True)
    participant_1 = Column("participant_1", User, nullable=False)
    participant_2 = Column("participant_2", User, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    message = relationship("Message", back_populates="chat")
    notification = relationship("Notification", back_populates="chat")
    attachment = relationship("Attachment", back_populates="chat")
    status_update = relationship("StatusUpdate", back_populates="chat")

    def __init__(self, chat_id, participant_1, participant_2, creation_date):
        self.chat_id = chat_id
        self.participant_1 = participant_1
        self.participant_2 = participant_2
        self.creation_date = creation_date
