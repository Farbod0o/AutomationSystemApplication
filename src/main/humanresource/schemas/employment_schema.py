from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class EmploymentCreate(BaseModel):
    startDate: date
    description: Optional[str] = Field(None, max_length=255)


class EmploymentResponse(EmploymentCreate):
    id: int

    class Config:
        from_attributes = True
