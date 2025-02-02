from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from model.da.data_access import Base


class ParaphStatus(Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    EXPIRED = "Expired"


class Paraph(Base):
    __tablename__ = "paraph_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paraph = Column(String(500), nullable=False)
    status = Column(Enum(ParaphStatus), nullable=False, default=ParaphStatus.ACTIVE)
    reference_id = Column(Integer, ForeignKey("reference_tbl.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=False)
    referral_date = Column(DateTime, nullable=False)
    expire_date = Column(DateTime, nullable=True)
    priority = Column(String(50), nullable=True)
    type = Column(String(50), nullable=True)
    confirmation = Column(String(50), nullable=True)

    reference = relationship("Reference", back_populates="paraphs")
    user = relationship("User", back_populates="paraphs")

def __init__(self, paraph, status, reference_id, user_id, referral_date, expire_date, priority, type,
             confirmation, reference, user):
    self.paraph = paraph
    self.status = status
    self.reference_id = reference_id
    self.user_id = user_id
    self.referral_date = referral_date
    self.expire_date = expire_date
    self.priority = priority
    self.type = type
    self.confirmation = confirmation
    self.reference = reference
    self.user = user
