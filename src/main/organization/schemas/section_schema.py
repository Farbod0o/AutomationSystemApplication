from pydantic import BaseModel, Field
from src.validators.regex_patterns import USERNAME_REGEX


class SectionCreate(BaseModel):
    head: str = Field(...,regex=USERNAME_REGEX)
    address: str = Field(..., regex=USERNAME_REGEX)
    name: str = Field(...,regex=USERNAME_REGEX)
    phoneNum: str = Field(...,regex=USERNAME_REGEX)
    internalCode: str = Field(..., regex=USERNAME_REGEX)
    description: str = Field(..., regex=USERNAME_REGEX)
    sectionNum: str = Field(..., regex=USERNAME_REGEX)
    accessLevel: str = Field(..., regex=USERNAME_REGEX)
    higherLevelSectionNum: str = Field(..., regex=USERNAME_REGEX)
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
