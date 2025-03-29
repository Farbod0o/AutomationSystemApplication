from pydantic import BaseModel, Field
from datetime import datetime


class TimeShiftCreate(BaseModel):
    total_hours: int = Field(..., max_length=5)


class TimeShiftResponse(TimeShiftCreate):
    id: int
    start_time: datetime | None
    end_time: datetime | None

    class Config:
        from_attributes = True
        