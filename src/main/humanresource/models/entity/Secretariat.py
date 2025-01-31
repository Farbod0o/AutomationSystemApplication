from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class Secretariat(Base):
    __tablename__ = "secretariat"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(100), nullable=False)
    _workflow_id = Column(Integer, ForeignKey('workflow.id'), nullable=False)
    _priority_id = Column(Integer, ForeignKey('workflow_priority.id'), nullable=False)

    workflow = relationship("Workflow", back_populates="secretariats")
    priority = relationship("WorkflowPriority", back_populates="secretariats")
    handled_requests = relationship("Letter", back_populates="secretariat")
    active_workflows = relationship("Workflow", back_populates="active_secretariat")

    def __init__(self, _name, _workflow_id, _priority_id):
        self._name = _name
        self._workflow_id = _workflow_id
        self._priority_id = _priority_id

    def __repr__(self):
        return f"<Secretariat(id={self._id}, name='{self._name}', workflow_id={self._workflow_id})>"
