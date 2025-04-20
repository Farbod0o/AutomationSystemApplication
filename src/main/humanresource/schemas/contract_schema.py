from pydantic import BaseModel, Field
from typing import Optional


class ContractCreate(BaseModel):
    name: str = Field(..., max_length=300)
    description: Optional[str] = Field(None, max_length=300)


class ContractResponse(BaseModel):
    id: int
    name:str
    description:str

    class Config:
        from_attributes = True
