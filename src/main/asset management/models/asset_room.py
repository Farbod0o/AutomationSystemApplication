from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class AssetRoom(Base):
    __tablename__ = "assetroom"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column(String, nullable=False)
    _description = Column(String, nullable=False)
    _address = Column(String, nullable=False)
    _phone = Column(String, nullable=True)

    assets = relationship("Asset", back_populates="asset_room")

    def __init__(self, title, description, address, phone):
        self.title = title
        self.description = description
        self.address = address
        self.phone = phone
