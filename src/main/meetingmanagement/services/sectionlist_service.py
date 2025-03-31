from src.main.meetingmanagement.models.sectionlist import SectionList
from src.main.organization.repositories.repository import Repository


def create_sectionList(sectionList_data):
    return True, Repository.save(sectionList_data, SectionList)

def get_sectionList_by_id(id):
    return True, Repository.find_by_id(SectionList, id)

def update_sectionList(sectionList_data):
    return True, Repository.update(sectionList_data, SectionList)

def delete_sectionList(id):
    Repository.delete(SectionList, id)
    return True, f"SectionList with id {id} deleted successfully."

def get_all_sectionLists():
    sectionsList = Repository.find_all(SectionList)
    return True, sectionsList
