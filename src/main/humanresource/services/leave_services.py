
from src.main.humanresource.models.entity.leave import Leave
from src.main.humanresource.repositories.repository import Repository


def create_leave(data):
    return True, Repository.save(data, Leave)


def get_leave_by_id(id):
    return True, Repository.find_by_id(Leave, id)


def get_all_leaves():
    leaves = Repository.find_all(Leave)
    return leaves


def delete_leave_by_id(id):
    return True, Repository.delete(id, Leave)


def update_leave(data):
    return True, Repository.update(data, Leave)

