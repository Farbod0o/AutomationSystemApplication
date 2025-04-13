from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from enum import Enum as PyEnum, Enum

class Status(PyEnum):
    SENT = "Sent"
    DELIVERED = "Delivered"
    SEEN = "Seen"

class StatusUpdate(Base):
    __tablename__ = "statusupdates"

    statusupdate_id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    status = Column("status", Enum(Status), nullable=False, default=Status.SENT)
    seen_time = Column("SeenTime", DateTime)

    chat = relationship("Chat", back_populates="statusupdates")

    def __init__(self, statusupdate_id, status, seenTime):
        self.statusupdate_id = statusupdate_id
        self.status = status
        self.seen_time = seenTime


