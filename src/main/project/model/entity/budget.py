from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from enum import Enum as PyEnum, Enum


class Status(PyEnum):
    PENDING = "Pending"
    APPROVED = "Approved"
    SPENT = "Spent"


class Budget(Base):
    __tablename__ = "budgets"

    budget_id = Column("budget_ID", Integer, primary_key=True, autoincrement=True)
    description = Column("description", String(100), nullable=False)
    amount = Column("amount", Float, nullable=False)
    allocation_date = Column("allocation_date", DateTime, nullable=False)
    status = Column("status", Enum(Status), nullable=False, default=Status.PENDING)

    ### relaitions to do

    def __init__(self, budget_id, description, amount, allocation_date, status):
        self.budget_id = budget_id
        self.description = description
        self.amount = amount
        self.allocation_date = allocation_date
        self.status = status
