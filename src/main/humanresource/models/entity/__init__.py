from sqlalchemy import Column, Integer, String, Date, ForeignKey,Float
from sqlalchemy.orm import relationship

from model.entity.base import Base

from model.entity.administrativerulings import AdministrativeRulings
from model.entity.contract import Contract
from model.entity.contract_type import ContractType
from model.entity.employment import Employment
from model.entity.insurance import Insurance
from model.entity.loan import Loan
from model.entity.tax import Tax
