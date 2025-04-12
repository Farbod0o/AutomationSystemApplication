from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class LoanCreate(BaseModel):
    start_date: date
    total_amount: int
    number_of_installment: int
    installment_amount: int
    registration_date: date
    status: str = Field(None, max_lenght=30)


class LoanResponse(LoanCreate):
    id: int

    class Config:
        from_attributes = True


