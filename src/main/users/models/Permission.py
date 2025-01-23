from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.main.database.da import Base
from .associations import role_permission_table


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    roles = relationship("Role", secondary=role_permission_table, back_populates="permissions")

    def __init__(self, name):
        self.name = name
