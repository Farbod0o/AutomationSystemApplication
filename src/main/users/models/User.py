from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from src.main.users.models.associations import user_role_table


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column("username", String(100), unique=True, nullable=False)
    password = Column("password", String(100), nullable=False)
    status = Column(Boolean, default=True)
    lastLogin = Column(DateTime, default=datetime.now)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Person", back_populates="user")
    roles = relationship("Role", secondary=user_role_table, back_populates="users")

    def __init__(self, username, password, status=True):
        self.username = username
        self.password = password
        self.status = status
        # self.person_id = person_id

