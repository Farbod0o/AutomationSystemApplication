from pydantic import BaseModel, Field


class TopicCreate(BaseModel):
    name: str = Field(..., max_length=30)
    description: str = Field(..., max_length=100)
    urgency: str = Field(..., max_length=30)


class TopicResponse(BaseModel):
    id: int
    name: str
    description: str
    urgency: str

    class Config:
        from_attributes = True
