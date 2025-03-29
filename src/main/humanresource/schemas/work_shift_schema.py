from pydantic import BaseModel, Field


class WorkShiftSchemaCreate(BaseModel):
    name: str = Field(..., max_lenght=100)
    time_shift_id: int


class WorkShiftSchemaResponse(WorkShiftSchemaCreate):
    id: int
    status: bool

    class Config:
        from_attributes = True
