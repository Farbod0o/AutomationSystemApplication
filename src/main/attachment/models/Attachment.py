from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table


class Attachment(Base):
    __tablename__ = "attachment"
    sent_date= Column("sent_date", datetime, nullable=False)
    sender = Column("sender", User, nullable=False)
    file = Column("file",Boolean,  nullable=True)
    file_size= Column("file_size", Integer, nullable=False)
    file_format = Column("file_format", String, nullable=False)

    def __init__(self, sent_date, sender, file, file_size, file_format):
        self.sent_date = sent_date
        self.sender = sender
        self.file = file
        self.file_size = file_size
        self.file_format = file_format
