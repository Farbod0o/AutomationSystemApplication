from pydantic import BaseModel, Field


class WorkShiftSchemaCreate(BaseModel):
    name: str = Field(..., max_lenght=100)
    time_shift_id: int


class WorkShiftSchemaResponse(BaseModel):
    id: int
    name: str
    status: bool
    time_shift_id: int

    class Config:
        from_attributes = True
