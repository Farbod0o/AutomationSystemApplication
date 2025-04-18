from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.models.personlist import PersonList
from src.main.meetingmanagement.schemas.personlist_schema import PersonListCreate, PersonListResponse
from src.main.meetingmanagement.services.personlist_service import create_PersonList, get_PersonList_by_id

router = APIRouter(prefix="/personlist", tags=["PersonLists"])

@router.post("/", response_model=PersonListResponse)
def create_new_personlist(personlist_data: PersonListCreate):
    new_personlist = PersonList(
        listName=personlist_data.listName
    )
    created = create_PersonList(new_personlist)[1]
    return PersonListResponse(**jsonable_encoder(created))

@router.get("/{personlist_id}", response_model=PersonListResponse)
def read_personlist(personlist_id: int):
    return get_PersonList_by_id(personlist_id)
