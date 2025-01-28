from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class ArchiveItem(Base):
    __tablename__ = "Archive_item"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(30), nullable=False)
    lastAccessed = Column("lastAccessed", DateTime, nullable=False)
    location = Column("location", String(50), nullable=False)

    def __init__(self, name, lastAccessed, location):
        self.name = name
        self.lastAccessed = lastAccessed
        self.location = location
