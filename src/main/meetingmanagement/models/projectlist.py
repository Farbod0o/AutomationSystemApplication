from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.main.database.da import Base

class Projectlist(Base):
    __tablename__ = 'project_list'
    id = Column("id",String, primary_key=True)
    project_name = Column("projectname",String(30), primary_key=True)
    projects=relationship("Project",backref="Projectlist")

    def __init__(self, project_name,projects):
        self.project_name = project_name
        self.projects =[projects]
