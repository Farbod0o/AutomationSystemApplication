from src.main.chat.models.entity.message import Message
from src.main.chat.models.repository.crud_repository import Repository


def create_message(message_data):
    return True, Repository.save(message_data, Message)


def get_message_by_id(message_id):
    return True, Repository.find_by_id(Message, message_id)


def update_message(message_data):
    return True, Repository.update(message_data, Message)


def delete_message(message_id):
    Repository.delete(Message, message_id)
    return True, f"message with id {id} deleted successfully."


def get_all_messages():
    messages = Repository.find_all(Message)
    return True, messages
