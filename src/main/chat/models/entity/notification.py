from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table


class Notification(Base):
    __tablename__ = "notification_tbl"

    _notification_id = Column(Integer, primary_key=True,autoincrement=True)
    _title = Column("title", String(50), nullable=False)
    _content = Column("content", String(50), nullable=False)
    _notification_type = Column("type", String(50), nullable=False)
    _target_user = Column("target_user", String(50), nullable=False)
    _creation_time = Column(DateTime, default=datetime.now)

    chat_id = Column(Integer, ForeignKey('chat_id'))
    chat = relationship("Chat", back_populates="notification")

    message_id = Column(Integer, ForeignKey("message_id"))
    message = relationship("Message", back_populates="notification_tbl")

    def __init__(self, title, content, notification_type, target_user, creation_time):
        self._title = title
        self._content = content
        self._notification_type = notification_type
        self._target_user = target_user
        self._creation_time = creation_time
