from sqlalchemy import Column,Integer,String
from src.main.database.da import Base
from sqlalchemy.orm import relationship



class WorkflowStepStatus(Base):
    __tablename__ = "workflow_step_status"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(50), unique=True, nullable=False)



    steps = relationship("WorkflowStep", back_populates="status")




    def __init__(self, _name):
        self._name = _name




    def __repr__(self):
        return f"<WorkflowStepStatus(id={self._id}, name='{self._name}')>"




