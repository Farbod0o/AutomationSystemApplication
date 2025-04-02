from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.organization.schemas.department_schema import DepartmentCreate, DepartmentResponse
from src.main.organization.services.department_service import create_department, get_department_by_id
from src.main.organization.models.department import Department

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.post("/", response_model=DepartmentResponse)
def create_new_department(department : DepartmentCreate):
    new_department = (Department
        (
        manager=department.manager,
        address=department.address,
        phoneNum=department.phoneNum,
        logo=department.logo,
        task=department.task,
        departmentNum=department.departmentNum,
        description=department.description)
    )
    department_data = jsonable_encoder(create_department(new_department)[1])
    department_response = DepartmentResponse(**department_data)
    return department_response


@router.get("/{department_id}", response_model=DepartmentResponse)
def read_department(department_id: int):
    return get_department_by_id(department_id)
