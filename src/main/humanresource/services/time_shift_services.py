
from src.main.humanresource.models.entity.time_shift import TimeShift
from src.main.humanresource.repositories.repository import Repository


def create_time_shift(data):
    return True, Repository.save(data, TimeShift)


def get_time_shift_by_id(id):
    return True, Repository.find_by_id(TimeShift, id)


def get_all_time_shifts():
    time_shifts = Repository.find_all(TimeShift)
    return time_shifts


def delete_time_shift(id):
    return True, Repository.delete(TimeShift, id)


def update_time_shift(data):
    return True, Repository.update(data, TimeShift)

