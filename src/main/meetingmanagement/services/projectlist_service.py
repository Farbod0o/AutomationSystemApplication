from src.main.meetingmanagement.models.projectlist import Projectlist
from src.main.meetingmanagement.repositories.repository import Repository


def create_projectlist(projectlist_data):
    return True, Repository.save(projectlist_data, Projectlist)

def get_projectlist_by_id(id):
    return True, Repository.find_by_id(Projectlist, id)

def update_projectlist(projectlist_data):
    return True, Repository.update(projectlist_data, Projectlist)

def delete_projectlist(id):
    Repository.delete(Projectlist, id)
    return True, f"Projectlist with id {id} deleted successfully."

def get_all_projectlists():
    projectlists = Repository.find_all(Projectlist)
    return True, projectlists