from pydantic import BaseModel, Field
from datetime import datetime
from src.validators.regex_patterns import USERNAME_REGEX, PASSWORD_REGEX


class UserCreate(BaseModel):
    username: str = Field(..., max_length=100, regex=USERNAME_REGEX)
    password: str = Field(..., min_length=6, regex=PASSWORD_REGEX)
    person_id: int

class UserResponse(BaseModel):
    id: int
    username: str
    status: bool
    lastLogin: datetime | None
    person_id: int

    class Config:
        from_attributes = True
