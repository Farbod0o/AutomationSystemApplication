from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class TicketGroup(Base):
    __tablename__ = ('ticketgroup')
    _id = Column(Integer,primary_key=True, autocrement=True)
    _name = Column(String(100), nullable=False)
    _parent_id = Column(Integer, ForeignKey('ticket_group.id'), nullable=True)
    _child_id = Column(Integer, ForeignKey('ticket_group.id'), nullable=True)

    parent = relationship('TicketGroup', remote_side=id)

    def __init__(self, name, parent_id, child_id):
        self.name = name
        self.parent_id = parent_id
        self.child_id = child_id