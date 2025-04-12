from src.main.humanresource.models.entity.loan import Loan
from src.main.humanresource.repositories.repository import Repository


def create_loan(data):
    return True, Repository.save(data, Loan)


def get_loan_by_id(id):
    return True, Repository.find_by_id(Loan, id)


def get_all_loans():
    loans = Repository.find_all(Loan)
    return loans


def delete_loan(id):
    return True, Repository.delete(id, Loan)


def update_loan(data):
    return True, Repository.update(data, Loan)
