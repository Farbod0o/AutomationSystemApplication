from src.main.database.da import Base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship



class WorkflowStep(Base):
    __tablename__ = "workflow_step"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(100), nullable=False)
    _description = Column(String(100), nullable=False)
    _status_id = Column(Integer, ForeignKey('workflow_step_status.id'), nullable=False)
    _priority_id = Column(Integer, ForeignKey('workflow_step_priority.id'), nullable=False)

    workflow = relationship("Workflow", back_populates="steps")
    status = relationship("WorkflowStepStatus", back_populates="steps")
    priority = relationship("WorkflowStepPriority", back_populates="steps")




    def __init__(self, _name, _description , _status_id ,_priority_id):
        self._name = _name
        self._description = _description
        self._status_id = _status_id
        self._priority_id = _priority_id






    def __repr__(self):
        return f"<WorkflowStep(id={self._id}, name='{self._name}', workflow_id={self._workflow_id})>"

