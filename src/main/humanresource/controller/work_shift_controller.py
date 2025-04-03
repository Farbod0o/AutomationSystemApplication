from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from src.main.humanresource.schemas.work_shift_schema import WorkShiftCreate, WorkShiftResponse
from src.main.humanresource.services.work_shift_services import create_work_shift, get_work_shift_by_id
from src.main.humanresource.models.entity.work_shift import WorkShift


router = APIRouter(prefix="/work_shift", tags=["work_shift"])


@router.post("/", response_model=WorkShiftResponse)
def create_new_work_shift(work_shift: WorkShiftCreate):
    new_work_shift = WorkShift(**work_shift.dict())
    work_shift_data = jsonable_encoder(create_work_shift(new_work_shift)[1])
    work_shift_response = WorkShiftResponse(**work_shift_data)
    return work_shift_response


@router.get("/{work_shift_id}", response_model=WorkShiftResponse)
def read_work_shift(work_shift_id: int):
    return get_work_shift_by_id(work_shift_id)