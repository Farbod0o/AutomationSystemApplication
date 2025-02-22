from src.main.users.models.Role import Role
from src.main.users.repositories.repository import Repository


def create_role(role_data):
    return True, Repository.save(role_data, Role)


def get_role_by_id(id):
    return True, Repository.find_by_id(Role, id)


def update_role(role_data):
    return True, Repository.update(role_data, Role)


def delete_role(id):
    Repository.delete(Role, id)
    return True, f"Role with id {id} deleted successfully."


def get_all_roles():
    roles = Repository.find_all(Role)
    return True, roles
