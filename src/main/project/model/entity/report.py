from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from enum import Enum as PyEnum, Enum


class Status(PyEnum):
    PLANNED = "Planned"
    INPROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"


class Type(PyEnum):
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    DAILY = "Daily"
    FINALS = "Finals"
    INCIDENT = "Incident"


class Report(Base):
    __tablename__ = "tasks"

    report_id = Column("report_ID", Integer, primary_key=True, autoincrement=True)
    author = Column("author", Integer, ForeignKey("users.id"), nullable=False)
    type = Column("type", Enum(Type), nullable=False, default=Type.DAILY)
    name = Column("task_name", String(30), nullable=False)
    description = Column("description", String(100), nullable=False)
    status = Column("status", Enum(Status), nullable=False, default=Status.PLANNED)
    date = Column("date", DateTime, nullable=False)

    ### relaitions to do

    def __init__(self, report_id, author, type, name, description, status, date):
        self.report_id = report_id
        self.author = author
        self.type = type
        self.name = name
        self.description = description
        self.status = status
        self.date = date
