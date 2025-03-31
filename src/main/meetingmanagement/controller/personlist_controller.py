from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.schemas.personlist_schema import PersonListCreate, PersonListResponse
from src.main.meetingmanagement.services.personlist_service import create_PersonList, get_PersonList_by_id
from src.main.meetingmanagement.models.personlist import PersonList

router = APIRouter(prefix="/PersonList", tags=["PersonLists"])


@router.post("/", response_model=PersonListResponse)
def create_new_PersonList(PersonList: PersonListCreate):
    new_PersonList = PersonList(listName=PersonList.listName)
    PersonList_data = jsonable_encoder(create_PersonList(new_PersonList)[1])
    PersonList_response = PersonListResponse(**PersonList_data)
    return PersonList_response


@router.get("/{PersonList_id}", response_model=PersonListResponse)
def read_PersonList(PersonList_id: int):
    return get_PersonList_by_id(PersonList_id)
