from src.main.database.da import Base
from sqlalchemy import Column, Integer, String


class Workflow(Base):
    __tablename__ = "workflow"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _name = Column(String(50))

    def __init__(self, _name):
        self._name = _name

    def __repr__(self):
        return f"<workflow {self._id}, '{self._name}'>"
