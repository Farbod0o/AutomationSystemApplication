from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.meetingmanagement.models.projectlist import Projectlist
from src.main.meetingmanagement.schemas.projectlist_schema import ProjectlistCreate, ProjectlistResponse
from src.main.meetingmanagement.services.projectlist_service import create_projectlist, get_projectlist_by_id

router = APIRouter(prefix="/projectlists", tags=["Project Lists"])


@router.post("/", response_model=ProjectlistResponse)
def create_new_projectlist(projectlist: ProjectlistCreate):
    new_projectlist = Projectlist(
        id=projectlist.id,
        project_name=projectlist.project_name,
        projects=None
    )
    projectlist_data = jsonable_encoder(create_projectlist(new_projectlist)[1])
    return ProjectlistResponse(**projectlist_data)


@router.get("/{projectlist_id}", response_model=ProjectlistResponse)
def read_projectlist(projectlist_id: str):
    return get_projectlist_by_id(projectlist_id)[1]
