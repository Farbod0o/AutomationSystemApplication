from  src.main.database.da import Base
from sqlalchemy import Column,Integer,String


class Workflow(Base):
    __tablename__ = "workflow"
    id = Column(Integer, primary_key=True , autoincrement=True)
    name = Column(String(50))



    def __init__(self,name):
        self.name = name


    def __repr__(self):
        return f"<workflow {self.id}, '{self.name}'>"



