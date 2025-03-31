
from src.main.humanresource.models.entity.deductions_and_bonuses import DeductionsAndBonuses
from src.main.humanresource.repositories.repository import Repository


def create_deductions_and_bonuses_repository(data):
    return True, Repository.save(data, DeductionsAndBonuses)


def get_deductions_and_bonuses_by_id(id):
    return True, Repository.find_by_id(DeductionsAndBonuses, id)


def get_all_deductions_and_bonuses():
    deductions_and_bonuses = Repository.find_all(DeductionsAndBonuses)
    return deductions_and_bonuses


def delete_deductions_and_bonuses(id):
    return True, Repository.delete(DeductionsAndBonuses, id)


def update_deductions_and_bonuses(data):
    return True, Repository.update(data, DeductionsAndBonuses)

