from pydantic import BaseModel, Field


class WorkShiftCreate(BaseModel):
    name: str = Field(..., max_lenght=100)
    time_shift_id: int


class WorkShiftResponse(WorkShiftCreate):
    id: int
    status: bool

    class Config:
        from_attributes = True
