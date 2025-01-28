from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class ArchiveRoom(Base):
    __tablename__ = "Archive_room"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(30), nullable=False)
    status = Column("status", Boolean, nullable=False)
    storageCapacity = Column("storageCapacity", Boolean, nullable=False)
    usedStorage = Column("usedStorage", Boolean, nullable=False)
    #archive_id = Column(Integer, ForeignKey("archive_id"))
    # mahtab ino check kon bbin droste asan niaze bodanesh?
    def __init__(self, name, status, storageCapacity, usedStorage):
        self.name = name
        self.status = status
        self.storageCapacity = storageCapacity
        self.usedStorage = usedStorage
