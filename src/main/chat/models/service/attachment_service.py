from src.main.chat.models.entity.attachment import Attachment
from src.main.chat.models.repository.crud_repository import Repository


def create_attachment(attachment_data):
    return True, Repository.save(attachment_data, Attachment)


def get_attachment_by_id(attachment_id):
    return True, Repository.find_by_id(Attachment, attachment_id)


def update_attachment(attachment_data):
    return True, Repository.update(attachment_data, Attachment)


def delete_attachment(attachment_id):
    Repository.delete(Attachment, attachment_id)
    return True, f"attachment with id {id} deleted successfully."


def get_all_attachments():
    attachments = Repository.find_all(Attachment)
    return True, attachments
