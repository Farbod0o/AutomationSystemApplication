from src.main.humanresource.models.entity.tax import Tax
from src.main.humanresource.repositories.repository import Repository


def create_tax(data):
    return True, Repository.save(data, Tax)


def get_tax_by_id(id):
    return True, Repository.find_by_id(Tax, id)


def get_all_taxes():
    texas = Repository.find_all(Tax)
    return texas


def delete_tax(id):
    return True, Repository.delete(id, Tax)


def update_tax(data):
    return True, Repository.update(data, Tax)
