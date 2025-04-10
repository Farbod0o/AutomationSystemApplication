from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table

class Message(Base):
    __tablename__ = "message_tbl"

    _message_id = Column("id", Integer, primary_key=True, autoincrement=True)
    _send_date = Column("SendDate", DateTime)
    _sender = Column("Sender", String(30))
    _text = Column("Text", String(50))

    notification = relationship("Notification", uselist=False, back_populates="message_tbl")

    chat_id = Column(Integer, ForeignKey("chat_id"))
    chat = relationship("Chat", back_populates="message_tbl")
def __init__(self, send_date, sender, text):
    self._send_date = send_date
    self._sender = sender
    self._text = text


