from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.schemas.sectionlist_schema import SectionListCreate, SectionListResponse
from src.main.meetingmanagement.services.sectionlist_service import create_sectionList, get_sectionList_by_id
from src.main.meetingmanagement.models.sectionlist import SectionList

router = APIRouter(prefix="/sectionList", tags=["SectionLists"])


@router.post("/", response_model=SectionListResponse)
def create_new_sectionList(sectionList: SectionListCreate):
    new_sectionList = SectionList(
        listName=sectionList.listName
    )
    created = create_sectionList(new_sectionList)[1]
    return SectionListResponse(**jsonable_encoder(created))


@router.get("/{sectionList_id}", response_model=SectionListResponse)
def read_sectionList(sectionList_id: int):
    return get_sectionList_by_id(sectionList_id)
