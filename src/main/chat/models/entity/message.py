from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base


class Message(Base):
    __tablename__ = "message_tbl"

    message_id = Column("id", Integer, primary_key=True, autoincrement=True)
    send_date = Column("SendDate", DateTime)
    sender = Column("Sender", String(30))
    text = Column("Text", String(50))

    notification = relationship("Notification", uselist=False, back_populates="message_tbl")

    chat_id = Column(Integer, ForeignKey("chat_id"))
    chat = relationship("Chat", back_populates="message_tbl")

    def __init__(self, message_id, send_date, sender, text):
        self.message_id = message_id
        self.send_date = send_date
        self.sender = sender
        self.text = text
