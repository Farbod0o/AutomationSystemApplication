from pydantic import BaseModel, Field
from typing import Literal


class DeductionAndBonusesCreate(BaseModel):
    name: str = Field(..., min_length=3)
    description: str = Field(..., max_length=300)
    type: Literal["Deduction", "Bonus"]
    amount: int


class DeductionAndBonusesResponse(DeductionAndBonusesCreate):
    id: int
    is_insurance_applicable: bool
    is_tax_applicable: bool

    class Config:
        from_attributes = True
