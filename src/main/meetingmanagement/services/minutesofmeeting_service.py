from src.main.meetingmanagement.models.minutesofmeeting import MinutesOfMeeting
from src.main.organization.repositories.repository import Repository


def create_MinutesOfMeeting(MinutesOfMeeting_data):
    return True, Repository.save(MinutesOfMeeting_data, MinutesOfMeeting)

def get_MinutesOfMeeting_by_id(id):
    return True, Repository.find_by_id(MinutesOfMeeting, id)

def update_MinutesOfMeeting(MinutesOfMeeting_data):
    return True, Repository.update(MinutesOfMeeting_data, MinutesOfMeeting)

def delete_MinutesOfMeeting(id):
    Repository.delete(MinutesOfMeeting, id)
    return True, f"MinutesOfMeetingwith id {id} deleted successfully."

def get_all_MinutesOfMeetings():
    MinutesOfMeetings = Repository.find_all(MinutesOfMeeting)
    return True, MinutesOfMeetings
