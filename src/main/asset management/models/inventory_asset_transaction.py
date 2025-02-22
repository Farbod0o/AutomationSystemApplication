from sqlalchemy import Column, Integer, DateTime, Foreignkey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class InventoryAssetTransaction(Base):
    __tablename__ = "inventoryassettransaction"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _count = Column(Integer, nullable=False, default=0)
    _date_of_transaction = Column(DateTime, nullable=False)

    asset_id = Column(Integer, Foreignkey("asset.id"))

    assets = relationship("Asset", back_populates="inventory_asset_transaction")

    def __init__(self, count, date_of_transaction):
        self.count = count
        self.date_of_transaction = date_of_transaction
