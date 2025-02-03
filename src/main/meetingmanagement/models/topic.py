from sqlalchemy import Column, Integer, String
from src.main.database.da import Base
from projectlist import *

class Topic(Base):
    __tablename__ = 'topic'
    id = Column("id",Integer, primary_key=True)
    name = Column("name",String(30))
    description = Column("description",String(100))
    urgency=Column("urgent",String(30))

    def __init__(self, name, description,urgency):
        self.name = name
        self.description = description
        self.urgency = urgency

    def __str__(self):
        return f"Topic (Name: {self.name}, Description: {self.description}, urgent: {self.urgency})"
