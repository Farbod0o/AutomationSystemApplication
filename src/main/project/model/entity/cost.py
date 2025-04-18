from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base

class Cost(Base):
    __tablename__ = "costs"

    cost_id = Column("cost_ID", Integer, primary_key=True, autoincrement=True)
    item_name = Column("item_name", String(30), nullable=False)
    description = Column("description", String(100), nullable=False)
    amount = Column("amount", Float, nullable=False)
    date = Column("date", DateTime, nullable=False)

    #relations to do

    def __init__(self, item_name, description, amount, date):
        self.item_name = item_name
        self.description = description
        self.amount = amount
        self.date = date
