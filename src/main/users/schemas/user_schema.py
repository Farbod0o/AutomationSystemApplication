from pydantic import BaseModel


class UserCreate(BaseModel):
    userName: str
    password: str


class UserResponse(BaseModel):
    id: int
    userName: str
    status: bool

    class Config:
        from_attributes = True
