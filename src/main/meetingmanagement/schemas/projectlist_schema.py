from pydantic import BaseModel, Field


class ProjectlistCreate(BaseModel):
    id: str = Field(..., max_length=50)
    project_name: str = Field(..., max_length=30)

class ProjectlistResponse(BaseModel):
    id: str
    project_name: str

    class Config:
        from_attributes = True
