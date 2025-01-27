from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class ArchiveItemType(Base):
    __tablename__ = "ArchiveItemType"
    id = Column("id", Integer, primary_key=True)
    type = Column("type", String(50), nullable=False)
