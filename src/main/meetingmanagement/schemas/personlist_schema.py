from pydantic import BaseModel, Field
from src.validators.regex_patterns import USERNAME_REGEX


class PersonListCreate(BaseModel):
    listName: str = Field(...,regex=USERNAME_REGEX)
    minutesofmeeting_id: int

class PersonListResponse(BaseModel):
    id: int
    listName: str
    minutesofmeeting_id_id: int

    class Config:
        from_attributes = True
