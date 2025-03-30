from src.main.humanresource.models.entity.work_shift import WorkShift
from src.main.humanresource.repositories.repository import Repository


def create_work_shift(data):
    return True, Repository.save(data, WorkShift)


def get_work_shift_by_id(id):
    return True, Repository.find_by_id(WorkShift, id)


def get_all_work_shifts():
    work_shifts = Repository.find_all(WorkShift)
    return work_shifts


def delete_work_shift(id):
    Repository.delete(WorkShift, id)
    return True, f"work shift with id {id} deleted successfully."

