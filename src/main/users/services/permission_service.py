from src.main.users.models.Permission import Permission
from src.main.users.repositories.repository import Repository


def create_permission(permission_data):
    return True, Repository.save(permission_data, Permission)


def get_permission_by_id(id):
    return True, Repository.find_by_id(Permission, id)


def update_permission(permission_data):
    return True, Repository.update(permission_data, Permission)


def delete_permission(id):
    Repository.delete(Permission, id)
    return True, f"Permission with id {id} deleted successfully."


def get_all_permissions():
    permissions = Repository.find_all(Permission)
    return True, permissions
