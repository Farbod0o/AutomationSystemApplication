from src.main.meetingmanagement.models.meeting import Meeting
from src.main.organization.repositories.repository import Repository


def create_meeting(meeting_data):
    return True, Repository.save(meeting_data, Meeting)

def get_meeting_by_id(id):
    return True, Repository.find_by_id(Meeting, id)

def update_meeting(meeting_data):
    return True, Repository.update(meeting_data, Meeting)

def delete_meeting(id):
    Repository.delete(Meeting, id)
    return True, f"Meeting with id {id} deleted successfully."

def get_all_meetings():
    meetings = Repository.find_all(Meeting)
    return True, meetings
