from pydantic import BaseModel, Field
from datetime import datetime


class TimeShiftCreate(BaseModel):
    total_hours: int = Field(..., max_length=5)


class TimeShiftResponse(BaseModel):
    id: int
    start_time: datetime | None
    end_time: datetime | None
    total_hours: int

    class Config:
        from_attributes = True
        