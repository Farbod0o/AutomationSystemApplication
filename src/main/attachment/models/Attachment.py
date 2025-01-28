from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table


class Attachment(Base):
    __tablename__ = "attachment_tbl"

    _attachment_id = Column(Integer, primary_key=True, autoincrement=True)
    _sent_date = Column("sent_date", datetime, nullable=False)
    _sender = Column("sender", String(100), nullable=False)
    _file = Column("file", String(100),  nullable=True)
    _file_size = Column("file_size", float(4), nullable=False)
    _file_format = Column("file_format", String(100), nullable=False)

    chat_id = Column(Integer, ForeignKey('chat_id'))
    chat = relationship("Chat", uselist=False, back_populates="attachment_tbl")

    def __init__(self, sent_date, sender, file, file_size, file_format):
        self._sent_date = sent_date
        self._sender = sender
        self._file = file
        self._file_size = file_size
        self._file_format = file_format
