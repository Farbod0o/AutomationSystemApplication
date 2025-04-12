from src.main.chat.models.entity.chat import Chat
from src.main.chat.models.repository.crud_repository import Repository


def create_chat(chat_data):
    return True, Repository.save(chat_data, Chat)


def get_chat_by_id(chat_id):
    return True, Repository.find_by_id(Chat, chat_id)


def update_chat(chat_data):
    return True, Repository.update(chat_data, Chat)


def delete_chat(chat_id):
    Repository.delete(Chat, chat_id)
    return True, f"Chat with id {id} deleted successfully."


def get_all_chats():
    chats = Repository.find_all(Chat)
    return True, chats
