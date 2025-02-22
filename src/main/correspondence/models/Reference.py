from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from model.da.data_access import Base


class ReferenceStatus(Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    EXPIRED = "Expired"


class ReferenceType(Enum):
    INTERNAL = "Internal"
    EXTERNAL = "External"


class Reference(Base):
    __tablename__ = "reference_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reference_code = Column(String(50), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    notes = Column(String(500), nullable=True)
    referral_date = Column(DateTime, nullable=False)
    expire_date = Column(DateTime, nullable=True)
    paraph = Column(String(255), nullable=True)
    priority = Column(String(50), nullable=True)
    type = Column(Enum(ReferenceType), nullable=False, default=ReferenceType.INTERNAL)
    status = Column(Enum(ReferenceStatus), nullable=False, default=ReferenceStatus.ACTIVE)
    confirmation = Column(String(50), nullable=True)
    sender_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=True)

    sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_references")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="received_references")

def __init__(self, reference_code, description, notes, referral_date, expire_date, paraph, priority, type, status,
             confirmation, sender_id, receiver_id, sender, receiver  ):
    self.reference_code = reference_code
    self.description = description
    self.notes = notes
    self.referral_date = referral_date
    self.expire_date = expire_date
    self.paraph = paraph
    self.priority = priority
    self.type = type
    self.status = status
    self.confirmation = confirmation
    self.sender_id = sender_id
    self.receiver_id = receiver_id
    self.sender = sender
    self.receiver = receiver


