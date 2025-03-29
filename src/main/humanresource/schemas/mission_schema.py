from pydantic import BaseModel, Field
from datetime import datetime


class MissionCreate(BaseModel):
    origin: str = Field(..., max_length=100)
    distance: int = Field(..., max_length=10)
    travel_method: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    accommodation: str = Field(..., max_length=100)
    time_sheet_id = int
    time_shift_id = int


class MissionResponse(MissionCreate):
    id: int
    extended_time: datetime | None
    start_date: datetime | None
    end_date: datetime | None
    request_date: datetime | None

    class Config:
        from_attributes = True
