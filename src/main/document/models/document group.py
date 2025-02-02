from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.da.data_access import Base


class DocumentGroup(Base):
    __tablename__ = "document_group_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    parent_id = Column(Integer, ForeignKey("document_group_tbl.id"), nullable=True)

    parent = relationship("DocumentGroup", remote_side=[id], back_populates="children")
    children = relationship("DocumentGroup", back_populates="parent", cascade="all, delete-orphan")


def __init__(self, name, parent_id, parent, children ):
    self.name = name
    self.parent_id = parent_id
    self.parent = parent
    self.children = children


