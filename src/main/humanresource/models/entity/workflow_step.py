from src.main.database.da import Base
from sqlalchemy import Column,String,Integer



class WorkflowStep(Base):
    __tablename__ = "workflow_step"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(100), nullable=False)
    _description = Column(String(100), nullable=False)




    def __init__(self, _name, _description):
        self._name = _name
        self._description = _description




    def __repr__(self):
        return f"<WorkflowStep(id={self._id}, name='{self._name}'>)"


