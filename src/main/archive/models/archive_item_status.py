from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class ArchiveItemStatus(Base):
    id = Column("id", Integer, primary_key=True)
    archive_item_status_id= Column("id", Integer, primary_key=True)
    statusName = Column("statusName", String(30), nullable=False)

    def __init__(self, statusName):
        self.statusName = statusName
