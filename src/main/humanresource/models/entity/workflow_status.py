from src.main.database.da import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column


class WorkflowStatus(Base):
    __tablename__ = "workflow_status"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _status_name = Column(String(70), unique=True, nullable=False)

    workflows = relationship("Workflow", back_populates="status")


    def __init__(self, status_name):
        self._status_name = status_name


    def __repr__(self):
        return f"<WorkflowStatus(id={self._id}, name='{self._status_name}')>"


