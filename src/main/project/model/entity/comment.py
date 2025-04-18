from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.main.database.da import Base

class Comment(Base):
    __tablename__ = "comments"

    comment_id = Column("comment_ID", Integer, primary_key=True, autoincrement=True)
    author = Column("author", Integer, ForeignKey("users.id"), nullable=False)
    description = Column("description", String(100), nullable=False)
    date = Column("date", DateTime, nullable=False)

    # relationship to do

    def __init__(self, comment_id, author, description, date):
        self.comment_id = comment_id
        self.author = author
        self.description = description
        self.date = date

