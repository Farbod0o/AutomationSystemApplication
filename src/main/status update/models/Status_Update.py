from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table


class StatusUpdate(Base):
    __tablename__ = "statusupdate_tbl"
    _statusupdate_id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    _status = Column("status", String(50))
    _seen_time = Column("SeenTime", DateTime)

    chat = relationship("Chat", back_populates="statusupdate_tbl")

def __init__ (self, id, status, SeenTime):
    self._id = id
    self._status = status
    self._seen_time = SeenTime


