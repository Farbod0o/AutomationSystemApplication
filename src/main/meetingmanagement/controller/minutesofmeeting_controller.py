from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.schemas.minutesofmeeting_schema import MinutesOfMeetingCreate, MinutesOfMeetingResponse
from src.main.meetingmanagement.services.minutesofmeeting_service import create_MinutesOfMeeting, get_MinutesOfMeeting_by_id
from src.main.meetingmanagement.models.minutesofmeeting import MinutesOfMeeting

router = APIRouter(prefix="/MinutesOfMeeting", tags=["MinutesOfMeetings"])


@router.post("/", response_model=MinutesOfMeetingResponse)
def create_new_MinutesOfMeeting(MinutesOfMeeting: MinutesOfMeetingCreate):
    new_MinutesOfMeeting = MinutesOfMeeting(listName=MinutesOfMeeting.listName)
    MinutesOfMeeting_data = jsonable_encoder(create_MinutesOfMeeting(new_MinutesOfMeeting)[1])
    MinutesOfMeeting_response = MinutesOfMeetingResponse(**MinutesOfMeeting_data)
    return MinutesOfMeeting_response


@router.get("/{MinutesOfMeeting_id}", response_model=MinutesOfMeetingResponse)
def read_MinutesOfMeeting(MinutesOfMeeting_id: int):
    return get_MinutesOfMeeting_by_id(MinutesOfMeeting_id)
