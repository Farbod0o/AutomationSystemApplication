from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class AssetStatus(Base):
    __tablename__ = "assetstatus"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _statusname = Column(String, nullable=False)

    assets = relationship("Asset", back_populates="asset_status")

    def __init__(self, statusname):
        self.statusname = statusname
