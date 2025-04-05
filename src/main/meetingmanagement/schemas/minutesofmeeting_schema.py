from pydantic import BaseModel, Field


class MinutesOfMeetingCreate(BaseModel):
    author: str = Field(...,max_length=50)
    date: str = Field(..., max_length=50)
    description: str = Field(..., max_length=50)
    attendee_list: str = Field(..., max_length=50)
    invitee_list: str = Field(..., max_length=50)
    follow_up_list: str = Field(..., max_length=50)
    approver_list: str = Field(..., max_length=50)


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
