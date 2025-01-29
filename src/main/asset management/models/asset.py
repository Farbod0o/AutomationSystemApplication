from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class Asset(Base):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, default=0, nullable=False)
    reminder = Column(Integer, default=0, nullable=True)
    limit = Column(Integer, default=0, nullable=True)
    asset_room_id = Column(Integer, ForeignKey("asset_room.id"))
    asset_transaction_id = Column(Integer, ForeignKey("asset_transaction.id"))
    inventory_asset_transaction_id = Column(Integer, ForeignKey("inventory_asset_transaction.id"))

    asset_room = relationship("AssetRoom", back_populates="asset")
    transaction = relationship("AssetTransaction", back_populates="asset")
    inventory_transaction = relationship("InventoryAssetTransaction", back_populates="asset")


    def __init__(self, count, reminder, limit):
        self.count = count
        self.reminder = reminder
        self.limit = limit
