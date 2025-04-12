from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.main.humanresource.models.entity.base import Base

from src.main.humanresource.models.entity.administrativerulings import AdministrativeRulings
from src.main.humanresource.models.entity.contract import Contract
from src.main.humanresource.models.entity.contract_type import ContractType
from src.main.humanresource.models.entity.employment import Employment
from src.main.humanresource.models.entity.insurance import Insurance
from src.main.humanresource.models.entity.loan import Loan
from src.main.humanresource.models.entity.tax import Tax
