from model.entity import *


class Contract(Base):
    __tablename__ = 'contract'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50))
    description = Column("description", String(255))

    def __init__(self, name, description):
        self.id = None
        # نام قرارداد
        self.name = name
        # توضیحات
        self.description = description
