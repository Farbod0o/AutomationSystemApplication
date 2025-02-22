from model.entity import *


class Employment(Base):
    __tablename__ = 'employment'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    start_date = Column("start_date", Date)
    description = Column("description", String(255))

    def __init__(self, start_date, description):
        # شناسه
        self.id = None
        # تاریخ شروع
        self.start_date = start_date
        # توضیحات
        self.description = description
