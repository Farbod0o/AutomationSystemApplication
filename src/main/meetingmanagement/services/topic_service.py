from src.main.meetingmanagement.models.topic import Topic
from src.main.users.repositories.repository import Repository


def create_topic(topic_data):
    return True, Repository.save(topic_data, Topic)

def get_topic_by_id(id):
    return True, Repository.find_by_id(Topic, id)

def update_topic(topic_data):
    return True, Repository.update(topic_data, Topic)

def delete_topic(id):
    Repository.delete(Topic, id)
    return True, f"Topic with id {id} deleted successfully."

def get_all_topics():
    topics = Repository.find_all(Topic)
    return True, topics
