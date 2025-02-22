from pydantic import BaseModel, Field


class PermissionCreate(BaseModel):
    name: str = Field(..., max_length=100)


class PermissionResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
