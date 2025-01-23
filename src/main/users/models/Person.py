from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    family = Column(String(100), nullable=False)
    national_id = Column(String(10), unique=True, nullable=False)
    phone = Column(String(15), unique=True)
    email = Column(String(100), unique=True)
    address = Column(String(255))
    user = relationship("User", uselist=False, back_populates="person")

    def __init__(self, name, family, nationalId, birthDate=None, phone=None, email=None, address=None):
        self.name = name
        self.family = family
        self.nationalId = nationalId
        self.birthDate = birthDate
        self.phone = phone
        self.email = email
        self.address = address
