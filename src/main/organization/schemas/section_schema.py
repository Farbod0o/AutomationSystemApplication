from pydantic import BaseModel, Field
from src.validators.regex_patterns import PHONE_REGEX


class SectionCreate(BaseModel):
    head: str = Field(...,max_length=30)
    address: str = Field(..., max_length=50)
    name: str = Field(...,max_length=30)
    phoneNum: str = Field(...,pattern=PHONE_REGEX)
    internalCode: str = Field(..., max_length=50)
    description: str = Field(None , max_length=225)
    sectionNum: str = Field(..., max_length=50)
    accessLevel: str = Field(..., max_length=50)
    higherLevelSectionNum: str = Field(..., max_length=50)
    department_id : int

class SectionResponse(BaseModel):
    id: int
    head: str
    address: str
    name: str
    phoneNum : str
    internalCode: str
    description: str
    sectionNum: str
    accessLevel: str
    higherLevelSectionNum: str
    department_id: int

    class Config:
        from_attributes = True
