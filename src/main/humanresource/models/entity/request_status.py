from src.main.database.da import Base
from sqlalchemy import Column, Integer, String


class Requeststatus(Base):
    __tablename__ = "request_status"
    id = Column(Integer, primary_key=True , autoincrement=True)
    status = Column(String(50), nullable=False)


    def __init__(self , status):
        self.status = status


    def __repr__(self):
        return f"<RequestStatus(id={self.id}, status='{self.status}')>"
