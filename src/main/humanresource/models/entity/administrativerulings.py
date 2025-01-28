from model.entity import *


class AdministrativeRulings(Base):
    __tablename__ = 'administrativerulings'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50), nullable=False)
    description = Column("description", String(255),nullable=False)
    rulings_type = Column("rulings_type", String(50),nullable=False)
    salary = Column("salary", Float(30))

    def __init__(self, name, description, rulings_type, salary):
        self.id = None
        # اسم قانون اداری
        self.name = name
        # توضیحات
        self.description = description
        # نوع قانون
        self.rulings_type = rulings_type
        # حقوق این قانون
        self.salary = salary
