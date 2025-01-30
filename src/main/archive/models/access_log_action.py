from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from src.main.database.da import Base
from sqlalchemy.orm import relationship


class AccessLogAction(Base):
    id = Column("id", Integer, primary_key=True)
    access_log_action_id= Column("id", Integer, primary_key=True)
    actionName = Column("actionName", String(30), nullable=False)

    def __init__(self, actionName):
        self.actionName = actionName
