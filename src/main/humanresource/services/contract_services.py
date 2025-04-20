from src.main.humanresource.models.entity.contract import Contract
from src.main.humanresource.repositories.repository import Repository



def create_contract(contract_data):
    return True, Repository.save(contract_data, Contract)

def get_contract_by_id(id):
    return True, Repository.find_by_id(Contract, id)

def update_contract(contract_data):
    return True, Repository.update(contract_data, Contract)

def delete_contract(id):
    Repository.delete(Contract, id)
    return True, f"Contract with id {id} deleted successfully."

def get_all_contract():
    contracts = Repository.find_all(Contract)
    return True, contracts