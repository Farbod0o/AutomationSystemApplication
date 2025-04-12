from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.main.humanresource.schemas.tax_schema import TaxCreate, TaxResponse
from src.main.humanresource.services.tax_services import create_tax, get_tax_by_id
from src.main.humanresource.models.entity.tax import Tax

router = APIRouter(prefix="/tax", tags=["tax"])


@router.post("/", response_model=TaxResponse)
def create_new_tax(tax: TaxCreate):
    new_tax = Tax(**tax.dict())
    tax_data = jsonable_encoder(create_tax(new_tax)[1])
    tax_response = TaxResponse(**tax_data)
    return tax_response


@router.get("/{tax_id}", response_model=TaxResponse)
def read_tax(tax_id: int):
    return get_tax_by_id(tax_id)
