from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base


class Notification(Base):
    __tablename__ = "notification_tbl"

    notification_id = Column("notificatin_ID", Integer, primary_key=True,autoincrement=True)
    title = Column("title", String(50), nullable=False)
    content = Column("content", String(50), nullable=False)
    notification_type = Column("type", String(50), nullable=False)
    target_user = Column("target_user", String(50), nullable=False)
    creation_time = Column(DateTime, default=datetime.now)

    chat_id = Column(Integer, ForeignKey("chat_id"))
    chat = relationship("Chat", back_populates="notification")

    message_id = Column(Integer, ForeignKey("message_id"))
    message = relationship("Message", back_populates="notification_tbl")

    def __init__(self, notification_id, title, content, notification_type, target_user, creation_time):
        self.notification_id = notification_id
        self.title = title
        self.content = content
        self.notification_type = notification_type
        self.target_user = target_user
        self.creation_time = creation_time
