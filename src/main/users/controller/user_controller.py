from fastapi import APIRouter, Depends
from src.main.users.schemas.user_schema import UserCreate, UserResponse
from src.main.users.repositories.user_repository import create_user, get_user_by_id

from src.main.users.models.User import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate):
    new_user = User(username=user.userName, password=user.password)
    return create_user(new_user)


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    return get_user_by_id(user_id)
