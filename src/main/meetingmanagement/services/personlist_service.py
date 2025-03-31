from src.main.meetingmanagement.models.personlist import PersonList
from src.main.organization.repositories.repository import Repository


def create_PersonList(PersonList_data):
    return True, Repository.save(PersonList_data, PersonList)

def get_PersonList_by_id(id):
    return True, Repository.find_by_id(PersonList, id)

def update_PersonList(PersonList_data):
    return True, Repository.update(PersonList_data, PersonList)

def delete_PersonList(id):
    Repository.delete(PersonList, id)
    return True, f"PersonList with id {id} deleted successfully."

def get_all_PersonLists():
    person_lists = Repository.find_all(PersonList)  
    return True, person_lists