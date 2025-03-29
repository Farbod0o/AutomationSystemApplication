from pydantic import BaseModel, Field
from datetime import datetime


class AdministrativeCalendarCreateBaseModel(BaseModel):
    day_of_week: str = Field(..., max_length=100)
    time_shift_id = int
    time_sheet_id = int


class AdministrativeCalendarCreateModel(AdministrativeCalendarCreateBaseModel):
    id: int
    date: datetime | None
    start_time: datetime | None
    end_time: datetime | None
    ins_holiday: bool

    class Config:
        from_attributes = True
