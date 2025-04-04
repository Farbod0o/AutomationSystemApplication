from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.schemas.meeting_schema import MeetingCreate, MeetingResponse
from src.main.meetingmanagement.services.meeting_service import create_meeting, get_meeting_by_id
from src.main.meetingmanagement.models.meeting import Meeting

router = APIRouter(prefix="/meetings", tags=["Meetings"])


@router.post("/", response_model=MeetingResponse)
def create_new_meeting(meeting: MeetingCreate):
    new_meeting = Meeting(
        date=meeting.date,
        day_of_week=meeting.day_of_week,
        location=meeting.location,
        meeting_manager=meeting.meeting_manager,
        start_time=meeting.start_time,
        end_time=meeting.end_time,
        title=meeting.title,
        status=meeting.status,
        description=meeting.description,
        minutesofmeeting_id=meeting.minutesofmeeting_id
    )
    meeting_data = jsonable_encoder(create_meeting(new_meeting)[1])
    meeting_response = MeetingResponse(**meeting_data)
    return meeting_response


@router.get("/{meeting_id}", response_model=MeetingResponse)
def read_meeting(meeting_id: int):
    return get_meeting_by_id(meeting_id)

