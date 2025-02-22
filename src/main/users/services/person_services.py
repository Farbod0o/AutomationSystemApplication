from src.main.users.models.Person import Person
from src.main.users.repositories.repository import Repository


def create_person(person_data):
    return True, Repository.save(person_data, Person)


def get_person_by_id(id):
    return True, Repository.find_by_id(Person, id)


def update_person(person_data):
    return True, Repository.update(person_data, Person)


def delete_person(id):
    Repository.delete(Person, id)
    return True, f"Person with id {id} deleted successfully."


def get_all_persons():
    persons = Repository.find_all(Person)
    return True, persons
