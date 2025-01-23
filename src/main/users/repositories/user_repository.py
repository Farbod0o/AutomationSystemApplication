from src.main.users.models.User import User
from src.main.users.services.user_service import UserService


def create_user(user):
    return True, UserService.save(user, User)


def get_user_by_id(id):
    return True, UserService.find_by_id(id, User)
