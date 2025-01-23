from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table, role_permission_table


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    roleName = Column(String(100), unique=True, nullable=False)
    description = Column(String(100))

    users = relationship("User", secondary=user_role_table, back_populates="roles")
    permissions = relationship("Permission", secondary=role_permission_table, back_populates="roles")

    def __init__(self, roleName, description=None):
        self.roleName = roleName
        self.description = description

