from pydantic import BaseModel, Field
from datetime import datetime


class TimeSheetCreate(BaseModel):
    day_of_week: str = Field(..., max_length=100)
    absence_description: str = Field(..., max_length=100)


class TimeSheetResponse(TimeSheetCreate):
    id: int
    entry_time: datetime | None
    exit_time: datetime | None
    date: datetime | None
    is_absent: bool

    class Config:
        from_attributes = True
