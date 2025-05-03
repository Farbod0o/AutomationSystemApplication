from pydantic import BaseModel, Field
from typing import Optional

class ContractTypeCreate(BaseModel):
    name: str = Field(..., max_length=300)
    description: Optional[str] = Field(..., max_length=300)



class ContractTypeResponse(BaseModel):
    id: int
    name:str
    description:str
    status:bool

    class Config:
        from_attributes = True
