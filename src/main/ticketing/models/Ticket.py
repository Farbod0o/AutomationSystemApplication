from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.main.database.da import Base


class Ticket(Base):
    __tablename__ = 'ticket'

    _id = Column(Integer, primary_key=True)
    _title = Column('department_title', String(30), nullable=False, unique=True)
    _text = Column(String(250), nullable=False)
    _created_by = Column(Integer, ForeignKey('user.id'), nullable=False)
    _assigned_to = Column(Integer, ForeignKey('user.id'), nullable=False)
    _datetime = Column(DateTime, nullable=False)

    created_by = relationship('User', foreign_keys=_created_by)
    assigned_to = relationship('User', foreign_keys=_assigned_to)
    message = relationship('Message', back_populates='ticket')

    def __init__(self, title, text, created_by, assigned_to, datetime):
        self.title = title
        self.text = text
        self.created_by = created_by
        self.assigned_to = assigned_to
        self.datetime = datetime
