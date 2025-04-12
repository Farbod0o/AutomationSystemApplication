from src.main.chat.models.entity.status_update import StatusUpdate
from src.main.chat.models.repository.crud_repository import Repository


def create_statusupdate(statusupdate_data):
    return True, Repository.save(statusupdate_data, StatusUpdate)


def get_statusupdate_by_id(statusupdate_id):
    return True, Repository.find_by_id(StatusUpdate, statusupdate_id)


def update_statusupdate(statusupdate_data):
    return True, Repository.update(statusupdate_data, StatusUpdate)


def delete_statusupdate(statusupdate_id):
    Repository.delete(StatusUpdate, statusupdate_id)
    return True, f"status update with id {id} deleted successfully."


def get_all_statusupdates():
    statusupdates = Repository.find_all(StatusUpdate)
    return True, statusupdates
