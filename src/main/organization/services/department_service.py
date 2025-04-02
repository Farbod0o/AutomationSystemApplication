from src.main.organization.models.department import Department
from src.main.organization.repositories.repository import Repository


def create_department(department_data):
    return True, Repository.save(department_data , Department)

def get_department_by_id(id):
    return True, Repository.find_by_id(Department, id)

def update_department(department_data):
    return True, Repository.update(department_data, Department)

def delete_department(id):
    Repository.delete(Department, id)
    return True, f"Department with id {id} deleted successfully."

def get_all_departments():
    departments = Repository.find_all(Department)
    return True, departments