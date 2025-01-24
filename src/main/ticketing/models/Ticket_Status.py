from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class TicketStatus (Base):
    __tablename__ = ('ticketstatus')
    _id = Column(Integer, primary_key=True, autocrement=True)
    _statusName = Column(String(50), nullable=False)

    ticket = relationship('Ticket', backref='ticket_status')


    def __init__(self, statusname):
        self.statusName = statusname