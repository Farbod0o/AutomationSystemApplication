from src.main.database.da import Base
from sqlalchemy import Column, Integer, String


class Requeststatus(Base):
    __tablename__ = "request_status"
    _id = Column(Integer, primary_key=True , autoincrement=True)
    _status = Column(String(50), nullable=False)


    def __init__(self , _status):
        self._status = _status


    def __repr__(self):
        return f"<RequestStatus(id={self._id}, status='{self._status}')>"
