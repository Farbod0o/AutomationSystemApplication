from sqlalchemy import Column, Integer, String
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class WorkflowStepPriority(Base):
    __tablename__ = "workflowStepPriority"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(100), nullable=False)

    steps = relationship("WorkflowStep", back_populates="priority")

    def __init__(self, _name):
        self._name = _name




    def __repr__(self):
        return f"<WorkflowStepPriority(id={self._id}, name='{self._name}')>"

