from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.models.topic import Topic
from src.main.meetingmanagement.schemas.topic_schema import TopicCreate, TopicResponse
from src.main.meetingmanagement.services.topic_service import create_topic, get_topic_by_id

router = APIRouter(prefix="/topics", tags=["Topics"])


@router.post("/", response_model=TopicResponse)
def create_new_topic(topic: TopicCreate):
    new_topic = Topic(
        name=topic.name,
        description=topic.description,
        urgency=topic.urgency
    )
    topic_data = jsonable_encoder(create_topic(new_topic)[1])
    topic_response = TopicResponse(**topic_data)
    return topic_response


@router.get("/{topic_id}", response_model=TopicResponse)
def read_topic(topic_id: int):
    return get_topic_by_id(topic_id)[1]
