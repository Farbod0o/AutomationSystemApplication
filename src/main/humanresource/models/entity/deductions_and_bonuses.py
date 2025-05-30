from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class DeductionsAndBonuses(Base):
    __tablename__ = 'deductions_and_bonuses'

    _id = Column(Integer, primary_key=True)
    _name = Column(String(100))
    _type = Column(Enum("Deduction", "Bonus"))
    _description = Column(String(300))
    _amount = Column(Integer)
    _is_insurance_applicable = Column(Boolean)
    _is_tax_applicable = Column(Boolean)

    def __init__(self, name, type, description, amount, is_insurance_applicable, is_tax_applicable):
        self.name = name
        self.type = type
        self.description = description
        self.amount = amount
        self.is_insurance_applicable = is_insurance_applicable
        self.is_tax_applicable = is_tax_applicable

