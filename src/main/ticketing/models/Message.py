from sqlalchemy import Column, string, Integer, DateTime, Foreignkey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    title = Column("title", string(100), nullable=False, unique=True)
    text = Column("text", string(300), nullable=False)
    dateTime = Column(DateTime, nullable=False)


    ticket_id = Column(Integer, Foreignkey("tickets.id"))
    ticket = relationship("Ticket", back_populates="messages")
    
    user_id = Column(Integer, Foreignkey("users.id"))
    user = relationship("User", back_populates="messages")


    def __init__(self, title, text, dateTime):
        self.title = title
        self.text = text
        self.dateTime = dateTime



