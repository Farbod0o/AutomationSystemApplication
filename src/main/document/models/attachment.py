from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from model.da.data_access import Base


class FileType(PyEnum):
    PDF = "PDF"
    IMAGE = "Image"
    VIDEO = "Video"
    AUDIO = "Audio"
    OTHER = "Other"


class Visibility(PyEnum):
    PUBLIC = "Public"
    PRIVATE = "Private"
    RESTRICTED = "Restricted"


class Status(PyEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class Attachment(Base):
    __tablename__ = "attachment_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(255), nullable=False)
    file_type = Column(Enum(FileType), nullable=False)
    file_size = Column(Float, nullable=False)
    uploaded_date = Column(DateTime, nullable=False)
    linked_to_id = Column(Integer, ForeignKey("linked_entity_tbl.id"), nullable=False) 
    visibility = Column(Enum(Visibility), nullable=False, default=Visibility.PRIVATE)
    status = Column(Enum(Status), nullable=False, default=Status.ACTIVE)
    description = Column(String(500), nullable=True)

    linked_to = relationship("LinkedEntity", back_populates="attachments")


def __init__(self, file_name, file_type, file_size, uploaded_date, linked_to_id, visibility, status, description, linked_to ):
    self.file_name = file_name
    self.file_type = file_type
    self.file_size = file_size
    self.uploaded_date = uploaded_date
    self.linked_to_id = linked_to_id
    self.visibility = visibility
    self.status = status
    self.description = description
    self.linked_to = linked_to



