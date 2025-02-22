from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class AssetTransaction(Base):
    __tablename__ = "asset_transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, default=0, nullable=False)
    date_of_transaction = Column(DateTime, nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"))
    
    asset = relationship("Asset", back_populates="transactions")
    status = relationship("AssetStatus", back_populates="transactions")
    asset_room = relationship("AssetRoom", back_populates="transactions")

    def __init__(self, count, date_of_transaction):
        self.count = count
        self.date_of_transaction = date_of_transaction


