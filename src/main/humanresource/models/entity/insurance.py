from src.main.humanresource.models.entity import *


class Insurance(Base):
    __tablename__ = 'insurance'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50))
    description = Column("description", String(255))
    insurance_type = Column("insurance_type", String(50))
    policy_type = Column("policy_type", Integer, nullable=True)
    years_of_coverage = Column("years_of_coverage", Integer)

    def __init__(self, name, description, insurance_type, policy_number, years_of_coverage):
        self.id = None
        # نام بیمه
        self.name = name
        # توضیحات
        self.description = description
        # نوع بیمه
        self.insurance_type = insurance_type
        # شماره بیمه نامه
        self.policy_number = policy_number
        # سال های تحت پوشش بیمه
        self.years_of_coverage = years_of_coverage
