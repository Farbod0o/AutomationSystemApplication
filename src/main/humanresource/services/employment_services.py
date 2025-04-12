from src.main.humanresource.models.entity.employment import Employment
from src.main.humanresource.repositories.repository import Repository


def create_employment(data):
    return True, Repository.save(data, Employment)


def get_employment_by_id(id):
    return True, Repository.find_by_id(Employment, id)


def get_all_employments():
    employments = Repository.find_all(Employment)
    return employments


def delete_employment(id):
    return True, Repository.delete(Employment, id)


def update_employment(data):
    return True, Repository.update(data, Employment)


