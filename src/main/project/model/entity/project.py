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


class Project(Base):
    __tablename__ = "projects"

    project_id = Column("project_ID", Integer, primary_key=True, autoincrement=True)
    project_name = Column("name",  String(30), nullable=False)
    description = Column("description", String(100), nullable=False)
    status = Column("status",Enum(Status),nullable=False, default=Status.PLANNED)
    start_date = Column("start_date", DateTime, nullable=False)
    end_date = Column("end_date", DateTime, nullable=False)
    registration_date = Column("registration_date", DateTime, nullable=False)
    # approvers = Column("approvers", Integer, ForeignKey("users.id"), nullable=False)
    # priority = Column("priority", String(30), nullable=False)

    # message = relationship("", back_populates="")
    # notification = relationship("", back_populates="")
    # attachment = relationship("", back_populates="")
    # status_update = relationship("", back_populates="")
    #
    # user_id = Column(Integer, ForeignKey("users.id"))
    # user = relationship("User", back_populates="Chats")

    def __init__(self, project_id, project_name, description, status, start_date, end_date, registration_date):
        self.project_id = project_id
        self.project_name = project_name
        self.description = description
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.registration_date = registration_date

