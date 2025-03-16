from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class PersonCreate(BaseModel):
    name: str = Field(..., max_length=100)
    family: str = Field(..., max_length=100)
    national_id: str = Field(..., max_length=10)
    phone: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr] = Field(None, max_length=100)
    address: Optional[str] = Field(None, max_length=255)

class PersonResponse(BaseModel):
    id: int
    name: str
    family: str
    national_id: str
    phone: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]

    class Config:
        from_attributes = True
