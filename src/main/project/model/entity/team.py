from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base


class Team(Base):
    __tablename__ = "teams"

    team_id = Column("team_ID", Integer, primary_key=True, autoincrement=True)
    name = Column("team_name", String(30), nullable=False)
    description = Column("description", String(100), nullable=False)
    members = relationship("Team_Members", String(100), nullable=False) # Question ??????
    leader = Column("team_leader", Integer, ForeignKey("users.id"), nullable=False)


    ### relaitions to do

    def __init__(self, team_id, name, description, members, leader):
        self.team_id = team_id
        self.name = name
        self.description = description
        self.members = members
        self.leader = leader


