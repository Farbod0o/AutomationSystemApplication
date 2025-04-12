from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base


class Attachment(Base):
    __tablename__ = "attachments"

    attachment_id = Column(Integer, primary_key=True, autoincrement=True)
    sent_date = Column("sent_date", datetime, nullable=False)
    sender = Column("sender", String(100), nullable=False)
    file = Column("file", String(100), nullable=True)
    file_size = Column("file_size", float(4), nullable=False)
    file_format = Column("file_format", String(100), nullable=False)

    chat_id = Column(Integer, ForeignKey('chat_id'))
    chat = relationship("Chat", uselist=False, back_populates="attachments")

    def __init__(self, sent_date, sender, file, file_size, file_format):
        self.sent_date = sent_date
        self.sender = sender
        self.file = file
        self.file_size = file_size
        self.file_format = file_format
