from sqlalchemy import Integer,Column,String, DateTime
from src.main.database.da import Base




class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True , autoincrement=True)
    title = Column(String(200),  nullable=False)
    send_data_time = Column(DateTime, nullable=False)
    write_data_time = Column(DateTime, nullable=False)



    def __init__(self, title, send_data_time, write_data_time):
        self.title = title
        self.send_data_time = send_data_time
        self.write_data_time = write_data_time


    def __repr__(self):
        return f"<Request(id={self.id}, title='{self.title}', send_date_time={self.send_date_time})>"