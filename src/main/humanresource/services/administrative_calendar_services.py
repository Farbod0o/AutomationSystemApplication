
from src.main.humanresource.models.entity.administrative_calendar import AdministrativeCalendar
from src.main.humanresource.repositories.repository import Repository


def create_administrative_calendar(data):
    return True, Repository.save(data, AdministrativeCalendar)


def get_administrative_calendar_by_id(id):
    return True, Repository.find_by_id(AdministrativeCalendar, id)


def get_all_administrative_calendars():
    administrative_calendars = Repository.find_all(AdministrativeCalendar)
    return administrative_calendars


def delete_administrative_calendar(id):
    return True, Repository.delete(id, AdministrativeCalendar)


def update_administrative_calendar(data):
    return True, Repository.update(data, AdministrativeCalendar)

