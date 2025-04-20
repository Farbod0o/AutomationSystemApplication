from src.main.humanresource.models.entity.contract_type import ContractType
from src.main.humanresource.repositories.repository import Repository


def create_contract_type(contract_type_data):
    return True, Repository.save(contract_type_data, ContractType)


def get_contract_type_by_id(id):
    return True, Repository.find_by_id(ContractType, id)


def get_all_contract_types():
    contract_types = Repository.find_all(ContractType)
    return True,contract_types


def delete_contract_type(id):
    Repository.delete(ContractType, id)
    return True, f"Contract_Type with id {id} deleted successfully."


def update_contract_type(contract_type_data):
    return True, Repository.update(contract_type_data, ContractType)
