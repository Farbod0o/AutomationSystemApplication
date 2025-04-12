from src.main.chat.models.entity.notification import Notification
from src.main.chat.models.repository.crud_repository import Repository


def create_notification(notification_data):
    return True, Repository.save(notification_data, Notification)


def get_notification_by_id(notification_id):
    return True, Repository.find_by_id(Notification, notification_id)


def update_notification(notification_data):
    return True, Repository.update(notification_data, Notification)


def delete_notification(notification_id):
    Repository.delete(Notification, notification_id)
    return True, f"notification with id {id} deleted successfully."


def get_all_notifications():
    notifications = Repository.find_all(Notification)
    return True, notifications
