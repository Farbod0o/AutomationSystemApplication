from src.main.humanresource.models.entity import *


class Loan(Base):
    __tablename__ = 'loan'
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    start_date = Column("start_date", Date)
    total_amount = Column("total_amount", Integer)
    number_of_installments = Column("number_of_installments", Integer)
    installment_amount = Column("installment_amount", Integer)
    registration_date = Column("registration_date", Date)
    status = Column("status", String(30))

    def __init__(self, start_date, total_amount, number_of_installments, installment_amount, registration_date, status):
        self.id = None
        # تاریخ شروع وام
        self.start_date = start_date
        # مبلغ کل وام
        self.total_amount = total_amount
        # تعداد قسط
        self.number_of_installments = number_of_installments
        # مبلغ هر قسط
        self.installment_amount = installment_amount
        # تاریخ ثبت وام
        self.registration_date = registration_date
        # وضعیت وام
        self.status = status
