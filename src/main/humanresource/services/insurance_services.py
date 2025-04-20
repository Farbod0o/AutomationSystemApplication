from src.main.humanresource.models.entity.insurance import Insurance
from src.main.humanresource.repositories.repository import Repository

def create_insurance(insurance_data):
    return True, Repository.save(insurance_data, Insurance)

def get_insurance_by_id(id):
    return True, Repository.find_by_id(Insurance, id)

def update_insurance(insurance_data):
    return True, Repository.update(insurance_data, Insurance)

def delete_insurance(id):
    Repository.delete(Insurance, id)
    return True, f"Insurance with id {id} deleted successfully."

def get_all_insurances():
    insurances = Repository.find_all(Insurance)
    return True, insurances