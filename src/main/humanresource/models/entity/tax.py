from src.main.humanresource.models.entity import *


class Tax(Base):
    __tablename__ = 'tax'
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    description = Column("description", String(255))
    tax_type = Column("tax_type", String(255))


    def __init__(self, description, tax_type):
        self.id = None
        # توضیحات مالیات
        self.description = description
        # نوع مالیات
        self.tax_type = tax_type
