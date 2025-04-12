from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.humanresource.schemas.employment_schema import EmploymentResponse, EmploymentCreate
from src.main.humanresource.services.employment_services import create_employment, get_employment_by_id
from src.main.humanresource.models.entity.employment import Employment

router = APIRouter(prefix="/emploment", tags=["Employment"])


@router.post("/", response_model=EmploymentResponse)
def create_new_employment(employment: EmploymentCreate):
    new_employment = Employment(
        start_date=employment.startDate, description=employment.description,
    )
    employment_data = jsonable_encoder(create_employment(new_employment)[1])
    employment_response = EmploymentResponse(**employment_data)
    return employment_response


@router.get("/{employment_id}", response_model=EmploymentResponse)
def read_employment(employment_id: int):
    return get_employment_by_id(employment_id)
