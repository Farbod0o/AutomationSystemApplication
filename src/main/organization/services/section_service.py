from src.main.organization.models.section import Section
from src.main.organization.repositories.repository import Repository


def create_section(section_data):
    return True, Repository.save(section_data, Section)

def get_section_by_id(id):
    return True, Repository.find_by_id(Section, id)

def update_section(section_data):
    return True, Repository.update(section_data, Section)

def delete_section(id):
    Repository.delete(Section, id)
    return True, f"Section with id {id} deleted successfully."

def get_all_sections():
    sections = Repository.find_all(Section)
    return True, sections
