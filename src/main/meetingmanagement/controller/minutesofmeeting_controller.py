from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.schemas.minutesofmeeting_schema import MinutesOfMeetingCreate, MinutesOfMeetingResponse
from src.main.meetingmanagement.services.minutesofmeeting_service import create_MinutesOfMeeting, get_MinutesOfMeeting_by_id
from src.main.meetingmanagement.models.minutesofmeeting import MinutesOfMeeting

router = APIRouter(prefix="/minutesofmeeting", tags=["MinutesOfMeetings"])


@router.post("/", response_model=MinutesOfMeetingResponse)
def create_new_minutes_of_meeting(meeting_data: MinutesOfMeetingCreate):
    new_minutes = MinutesOfMeeting(listName=meeting_data.listName)
    minutes_data = jsonable_encoder(create_MinutesOfMeeting(new_minutes)[1])
    minutes_response = MinutesOfMeetingResponse(**minutes_data)
    return minutes_response


@router.get("/{minutes_id}", response_model=MinutesOfMeetingResponse)
def read_minutes_of_meeting(minutes_id: int):
    return get_MinutesOfMeeting_by_id(minutes_id)
