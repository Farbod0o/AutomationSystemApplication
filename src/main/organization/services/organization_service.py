from src.main.organization.models.organization import Organization
from src.main.organization.repositories.repository import Repository


def create_organization(organization_data):
    return True, Repository.save(organization_data, Organization)

def get_organization_by_id(id):
    return True, Repository.find_by_id(Organization, id)

def update_organization(organization_data):
    return True, Repository.update(organization_data, Organization)

def delete_organization(id):
    Repository.delete(Organization, id)
    return True, f"Organization with id {id} deleted successfully."

def get_all_organizations():
    organizations = Repository.find_all(Organization)
    return True, organizations