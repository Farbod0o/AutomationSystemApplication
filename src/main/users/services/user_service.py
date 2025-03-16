from src.main.users.models.User import User
from src.main.users.repositories.repository import Repository


def create_user(user_data):
    return True, Repository.save(user_data, User)

def get_user_by_id(id):
    return True, Repository.find_by_id(User, id)

def update_user(user_data):
    return True, Repository.update(user_data, User)

def delete_user(id):
    Repository.delete(User, id)
    return True, f"User with id {id} deleted successfully."

def get_all_users():
    users = Repository.find_all(User)
    return True, users
