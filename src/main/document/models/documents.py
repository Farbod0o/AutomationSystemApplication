from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from model.da.data_access import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=False)
    last_modified_by_id = Column(Integer, ForeignKey("user_tbl.id"), nullable=True)
    created_at = Column(DateTime, nullable=False)

    author = relationship("User", foreign_keys=[author_id], back_populates="documents_created")
    last_modified_by = relationship("User", foreign_keys=[last_modified_by_id], back_populates="documents_modified")

def __init__(self,title,content,author_id,last_modified_by_id,created_at):
    self.title = title
    self.content = content
    self.author_id = author_id
    self.last_modified_by_id = last_modified_by_id
    self.created_at = datetime.datetime.now()
