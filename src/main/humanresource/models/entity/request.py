from sqlalchemy import Integer,Column,String, DateTime ,ForeignKey
from src.main.database.da import Base
from sqlalchemy.orm import relationship




class Request(Base):
    __tablename__ = "requests"
    _id = Column(Integer, primary_key=True , autoincrement=True)
    _title = Column(String(200),  nullable=False)
    _send_data_time = Column(DateTime, nullable=False)
    _write_data_time = Column(DateTime, nullable=False)
    status_id = Column(Integer, ForeignKey('request_status.id'), nullable=False)
    priority_id = Column(Integer, ForeignKey('request_priority.id'), nullable=False)

    status = relationship('RequestStatus', backref='requests')
    priority = relationship('RequestPriority', backref='requests')



    def __init__(self, _title, _send_data_time, _write_data_time):
        self._title = _title
        self._send_data_time = _send_data_time
        self._write_data_time = _write_data_time



    def __repr__(self):
        return f"<Request(id={self._id}, title='{self._title}', send_date_time={self._send_date_time})>"