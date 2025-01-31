from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from src.main.database.da import Base


class WorkflowPriority(Base):
    __tablename__ = "workflow_priority"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(60), unique=True, nullable=False)


    workflows = relationship("Workflow", back_populates="priority")


    def __init__(self, _name):
        self._name = _name


    def __repr__(self):
        return f"<WorkflowPriority(id={self._id}, name='{self._name}')>"


