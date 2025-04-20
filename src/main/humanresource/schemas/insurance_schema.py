from pydantic import BaseModel, Field
from typing import Optional


class InsuranceCreate(BaseModel):
    name: str = Field(..., max_length=300)
    description: Optional[str] = Field(None, max_length=300)
    insurance_type: str = Field(..., max_length=300)
    policy_number: str = Field(..., max_length=300)


class InsuranceResponse(BaseModel):
    id: int
    name:str
    description:str
    insurance_type:str
    policy_number:str
    years_of_coverage:int

    class Config:
        from_attributes = True






