from pydantic import BaseModel, Field
from typing import List, Optional


class RoleCreate(BaseModel):
    roleName: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=100)

class RoleResponse(BaseModel):
    id: int
    roleName: str
    description: Optional[str]
    users: List[int]

    class Config:
        from_attributes = True
