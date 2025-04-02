from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.organization.schemas.organization_schema import OrganizationCreate, OrganizationResponse
from src.main.organization.services.organization_service import create_organization, get_organization_by_id
from src.main.organization.models.organization import Organization

router = APIRouter(prefix="/organizations", tags=["Organizations"])


@router.post("/", response_model=OrganizationResponse)
def create_new_organization(organization: OrganizationCreate):
    new_organization = Organization(
        manager=organization.manager,
        address=organization.address,
        phoneNum=organization.phoneNum,
        logo=organization.logo,
        task=organization.task,
        departmentNum=organization.departmentNum,
        description=organization.description
    )
    organization_data = jsonable_encoder(create_organization(new_organization)[1])
    organization_response = OrganizationResponse(**organization_data)
    return organization_response


@router.get("/{organization_id}", response_model=OrganizationResponse)
def read_organization(organization_id: int):
    return get_organization_by_id(organization_id)
