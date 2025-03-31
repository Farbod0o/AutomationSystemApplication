
from src.main.humanresource.models.entity.mission import Mission
from src.main.humanresource.repositories.repository import Repository


def create_mission(data):
    return True, Repository.save(data)


def get_mission_by_id(id):
    return True, Repository.find_by_id(Mission, id)


def get_all_missions():
    missions = Repository.find_all(Mission)
    return missions


def delete_mission(id):
    return True, Repository.delete(Mission, id)


def update_mission(data):
    return True, Repository.update(data, Mission)

