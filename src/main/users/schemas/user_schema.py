from pydantic import BaseModel, Field
from datetime import datetime


class UserCreate(BaseModel):
    userName: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    status: bool
    lastLogin: datetime | None

    class Config:
        orm_mode = True



