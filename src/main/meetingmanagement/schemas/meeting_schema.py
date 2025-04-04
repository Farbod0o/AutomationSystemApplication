from pydantic import BaseModel, Field
from datetime import date, time
from enum import Enum

class MeetingStatus(str, Enum):
    Scheduled = "Scheduled"
    Held = "Held"
    Canceled = "Canceled"

class MeetingCreate(BaseModel):
    date: date
    day_of_week: str = Field(..., max_length=20)
    location: str = Field(..., max_length=100)
    meeting_manager: str = Field(..., max_length=50)
    start_time: time
    end_time: time
    title: str = Field(..., max_length=100)
    status: MeetingStatus
    description: str | None = Field(default=None, max_length=255)
    minutesofmeeting_id: int

class MeetingResponse(MeetingCreate):
    id: int

    class Config:
        from_attributes = True
