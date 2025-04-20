from src.main.humanresource.models.entity.administrativerulings import AdministrativeRulings
from src.main.humanresource.repositories.repository import Repository

def create_administrative_rulings(administrative_rulings_data):
    return True, Repository.save(administrative_rulings_data, AdministrativeRulings)

def get_administrative_rulings_by_id(id):
    return True, Repository.find_by_id(AdministrativeRulings, id)

def update_administrative_rulings(administrative_rulings_data):
    return True, Repository.update(administrative_rulings_data, AdministrativeRulings)

def delete_administrative_rulings(id):
    Repository.delete(AdministrativeRulings, id)
    return True, f"Administrative_Rulings with id {id} deleted successfully."

def get_all_administrative_rulings():
    administrative_rulings = Repository.find_all(AdministrativeRulings)
    return True, administrative_rulings
