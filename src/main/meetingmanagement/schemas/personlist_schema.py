from pydantic import BaseModel, Field


class PersonListCreate(BaseModel):
    listName: str = Field(...,max_length=100)
    minutesofmeeting_id: int

class PersonListResponse(BaseModel):
    id: int
    listName: str
    minutesofmeeting_id_id: int

    class Config:
        from_attributes = True
