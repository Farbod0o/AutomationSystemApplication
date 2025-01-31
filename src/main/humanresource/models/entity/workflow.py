from src.main.database.da import Base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship


class Workflow(Base):
    __tablename__ = "workflow"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(50), unique=True, nullable=False)
    _priority_id = Column(Integer, ForeignKey('workflow_priority.id'), nullable=False)
    _status_id = Column(Integer, ForeignKey('workflow_status.id'), nullable=False)

    priority = relationship("WorkflowPriority", back_populates="workflows")
    status = relationship("WorkflowStatus", back_populates="workflows")
    steps = relationship("WorkflowStep", back_populates="workflow")
    secretariats = relationship("Secretariat", back_populates="workflow")
    active_secretariat = relationship("Secretariat", back_populates="active_workflows")

    def __init__(self, _name, _priority_id, _status_id):
        self._name = _name
        self._priority_id = _priority_id
        self._status_id = _status_id


    def __repr__(self):
        return f"<workflow {self._id}, '{self._name}'>"
