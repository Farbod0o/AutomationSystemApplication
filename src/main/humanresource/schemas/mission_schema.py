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


class MissionResponse(BaseModel):
    id: int
    extended_time: datetime | None
    origin: str
    start_date: datetime | None
    end_date: datetime | None
    distance: int
    request_date: datetime | None
    travel_method: str
    description: str
    accommodation: str
    time_sheet_id = int
    time_shift_id = int

    class Config:
        from_attributes = True
