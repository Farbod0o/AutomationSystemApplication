from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey ,Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base
from enum import Enum as PyEnum, Enum

class Status(PyEnum):
    PLANNED = "Planned"
    INPROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column("task_ID", Integer, primary_key=True, autoincrement=True)
    name = Column("task_name", String(30),  nullable=False)
    description = Column("description", String(100), nullable=False)
    status = Column("status",Enum(Status) ,nullable=False, default=Status.PLANNED)
    weight = Column(Float, nullable=False)
    assigned_to = Column("assigned_to", Integer, ForeignKey("users.id"), nullable=False)
    time_line = Column("time_line", DateTime, nullable=False) #to do

    ### relaitions to do

    def __init__(self, task_id, name, description, status, weight, assigned_to, time_line):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status
        self.weight = weight
        self.assigned_to = assigned_to
        self.time_line = time_line
