from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from enum import Enum as PyEnum, Enum

class Status(PyEnum):
    PLANNED = "Planned"
    INPROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class SubProject(Base):
    __tablename__ = "sub_projects"

    sub_project_id = Column("sub_project_ID", Integer, primary_key=True, autoincrement=True)
    name = Column("sub_project_name", String(30),  nullable=False)
    description = Column("description", String(100), nullable=False)
    status = Column("status",Enum(Status),nullable=False, default=Status.PLANNED)
    parent_project = Column("parent_project", Integer, ForeignKey("projects.id"), nullable=False)

    # message = relationship("", back_populates="")
    # notification = relationship("", back_populates="")
    # attachment = relationship("", back_populates="")
    # status_update = relationship("", back_populates="")

    # user_id = Column(Integer, ForeignKey("users.id"))
    # user = relationship("User", back_populates="Chats")

    def __init__(self, sub_project_id, name, description, status, parent_project):
        self.sub_project_id = sub_project_id
        self.name = name
        self.description = description
        self.status = status
        self.parent_project = parent_project
