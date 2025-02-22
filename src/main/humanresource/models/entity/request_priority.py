from src.main.database.da import Base
from sqlalchemy import Column,Integer,String


class RequestPriority(Base):
    __tablename__ = "request_priority"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _priority_name = Column(String(100), nullable=False)



    def __init__(self, _priority_name):
        self._priority_name = _priority_name


    def __repr__(self):
        return f"<RequestPriority({self._priority_name})>"



