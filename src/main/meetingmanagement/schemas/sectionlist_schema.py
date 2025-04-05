from pydantic import BaseModel, Field



class SectionListCreate(BaseModel):
    listName: str = Field(...,max_length=50)
    meeting_id: int

class SectionListResponse(BaseModel):
    id: int
    listName: str
    meeting_id: int

    class Config:
        from_attributes = True
