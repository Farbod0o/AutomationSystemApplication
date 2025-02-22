from model.entity import *


class ContractType(Base):
    __tablename__ = 'contract_type'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(30))
    description = Column("description", String(255))
    status = Column("status", String(30))

    def __init__(self, name, description, status):
        self.id = None
        # نام نوع قرارداد
        self.name = name
        # توضیحات
        self.description = description
        # وضعیت
        self.status = status
