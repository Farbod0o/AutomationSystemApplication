
from src.main.humanresource.models.entity.time_sheet import TimeSheet
from src.main.humanresource.repositories.repository import Repository


def create_time_sheet(data):
    return True, Repository.save(data, TimeSheet)


def get_time_sheet_by_id(id):
    return True, Repository.find_by_id(TimeSheet, id)


def get_all_time_sheets():
    time_sheets = Repository.find_all(TimeSheet)
    return time_sheets


def delete_time_sheet(id):
    return True, Repository.delete(TimeSheet, id)


def update_time_sheet(data):
    return True, Repository.update(data, TimeSheet)

