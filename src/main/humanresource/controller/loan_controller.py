from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.humanresource.schemas.loan_schema import LoanCreate, LoanResponse
from src.main.humanresource.services.loan_services import create_loan, get_loan_by_id
from src.main.humanresource.models.entity.loan import Loan

router = APIRouter(prefix="/loan", tags=["Loan"])


@router.post("/", response_model=LoanResponse)
def create_new_loan(loan: LoanCreate):
    new_loan = Loan(**loan.dict())
    loan_data = jsonable_encoder(create_loan(new_loan)[1])
    loan_response = LoanResponse(**loan_data)
    return loan_response


@router.get("/{loan_id}", response_model=LoanResponse)
def read_loan(loan_id: int):
    return get_loan_by_id(loan_id)
