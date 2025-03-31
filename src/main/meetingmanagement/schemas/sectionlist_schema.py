from pydantic import BaseModel, Field
from src.validators.regex_patterns import USERNAME_REGEX


class SectionListCreate(BaseModel):
    listName: str = Field(...,regex=USERNAME_REGEX)
    meeting_id: int

class SectionListResponse(BaseModel):
    id: int
    listName: str
    meeting_id: int

    class Config:
        from_attributes = True
