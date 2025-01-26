from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table


class Notification(Base):
    __tablename__ = "notification"
    title = Column("title", String(50), nullable=False)
    content = Column("content", String(50), nullable=False)
    notification_type = Column("type", enumerate(), nullable=False)
    target_user = Column("target_user", String(50), nullable=False)
    creation_time = Column(DateTime, default=datetime.now)

    def __init__(self, title, content, notification_type, target_user, creation_time):
        self.title = title
        self.content = content
        self.notification_type = notification_type
        self.target_user = target_user
        self.creation_time = creation_time
