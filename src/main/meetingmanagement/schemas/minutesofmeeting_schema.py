from pydantic import BaseModel, Field
from src.validators.regex_patterns import USERNAME_REGEX


class MinutesOfMeetingCreate(BaseModel):
    author: str = Field(...,regex=USERNAME_REGEX)
    date: str = Field(..., regex=USERNAME_REGEX)
    description: str = Field(..., regex=USERNAME_REGEX)
    attendee_list: str = Field(..., regex=USERNAME_REGEX)
    invitee_list: str = Field(..., regex=USERNAME_REGEX)
    follow_up_list: str = Field(..., regex=USERNAME_REGEX)
    approver_list: str = Field(..., regex=USERNAME_REGEX)


class MinutesOfMeetingResponse(BaseModel):
    id: int
    author: str
    date: str
    description: str
    attendee_list: str
    invitee_list: str
    follow_up_list: str
    approver_list: str


    class Config:
        from_attributes = True
