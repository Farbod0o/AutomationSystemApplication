from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class LeaveCreate(BaseModel):
    leave_type: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=100)


class LeaveResponse(LeaveCreate):
    id: int
    end_time: datetime | None
    start_date: datetime | None
    end_date: datetime | None
    status: bool
    registration_date: datetime | None
    time_shift_id: int
    time_sheet_id: int

    class Config:
        from_attributes = True
