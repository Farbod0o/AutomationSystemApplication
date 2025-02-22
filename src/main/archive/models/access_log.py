from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class AccessLog(Base):
    __tablename__ = "AccessLog"
    id = Column("id", Integer, primary_key=True)
    access_log_id= Column("id", Integer, primary_key=True)
    accessDate = Column("accessDate", DateTime, nullable=False)

    def __init__(self, accessDate):
        self.accessDate = accessDate
