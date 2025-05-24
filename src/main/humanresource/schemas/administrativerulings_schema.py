from pydantic import BaseModel, Field
from typing import Optional


class AdministrativeRulingsCreate(BaseModel):
    name: str = Field(..., max_length=300)
    description: Optional[str] = Field(..., max_length=300)
    administrativerulings_type: str = Field(..., max_length=300)
    salary: int = Field(..., max_length=100)


class AdministrativeRulingsResponse(BaseModel):
    id: int
    name:str
    description:str
    administrativerulings_type: str
    salary:int

    class Config:
        from_attributes = True


