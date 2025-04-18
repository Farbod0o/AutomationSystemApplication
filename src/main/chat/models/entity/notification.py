from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from enum import Enum as PyEnum, Enum


class NotifType(PyEnum):
    MESSAGE = "Message"
    REMINDER = "Reminder"
    ALERT = "Alert"

class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column("notificatin_ID", Integer, primary_key=True,autoincrement=True)
    title = Column("title", String(50), nullable=False)
    content = Column("content", String(50), nullable=False)
    notification_type = Column("notification_type", Enum(NotifType), nullable=False, default=NotifType.MESSAGE)
    target_user = Column("target_user", Integer, ForeignKey("users.id"), nullable=False)
    creation_time = Column(DateTime, default=datetime.now)

    chat_id = Column(Integer, ForeignKey("chat_id"))
    chat = relationship("Chat", back_populates="notifications")

    message_id = Column(Integer, ForeignKey("message_id"))
    message = relationship("Message", back_populates="notifications")

    def __init__(self, notification_id, title, content, notification_type, target_user, creation_time):
        self.notification_id = notification_id
        self.title = title
        self.content = content
        self.notification_type = notification_type
        self.target_user = target_user
        self.creation_time = creation_time
