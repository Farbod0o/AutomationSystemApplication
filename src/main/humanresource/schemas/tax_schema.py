from pydantic import BaseModel, Field
from typing import Optional


class TaxCreate(BaseModel):
    description: Optional[str] = Field(None, max_lenght=255)
    tax_type: Optional[str] = Field(None, max_lenght=255)


class TaxResponse(TaxCreate):
    id: int

    class Config:
        from_attributes = True
