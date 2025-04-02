from pydantic import BaseModel, Field
from src.validators.regex_patterns import PHONE_REGEX


class OrganizationCreate(BaseModel):
    manager: str = Field(..., max_length=50)
    name: str = Field(..., max_length=50)
    address: str = Field(..., max_length=100)
    phoneNum: str = Field(..., pattern=PHONE_REGEX)
    logo: str = Field(..., max_length=50)
    task: str = Field(..., max_length=50)
    departmentNum: str = Field(..., max_length=50)
    description: str = Field(..., max_length=100)
    department_id: int

    class Config:
        from_attributes = True


class OrganizationResponse(BaseModel):
    id: int
    manager: str
    name: str
    address: str
    phoneNum: str
    logo: str
    task: str
    departmentNum: str
    description: str

    class Config:
        from_attributes = True
