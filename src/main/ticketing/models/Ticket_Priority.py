from sqlalchemy import Column, string, Integer, DateTime, Foreignkey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base

class TicketPriority(Base):
    __tablename__ = "ticketpriority"
    id = Column(Integer, primary_key=True)
    priorityName = Column(string(50), nullable=False)

    ticket = relationship("Ticket", back_populates="priority")
    
    
    def __init__(self, priorityname):
        self.priorityName = priorityname
