from sqlalchemy import Column, Integer, String, Date, column
from sqlalchemy.orm import relationship

from src.main.database.da import Base


class MinutesOfMeeting(Base):
    __tablename__ = 'Minutes_Of_Meeting'
    id = Column(Integer, primary_key=True)
    author = Column("author",String(30),nullable=False)
    date = Column("date",Date,nullable=False)
    description = Column("description",String(255))
    attendee_list=Column("attendee_list",String(255),nullable=True)
    invitee_list=Column("invitee_list",String(255),nullable=True)
    follow_up_list=Column("follow_up_list",String(255),nullable=True)
    approver_list=Column("approve_list",String(255),nullable=True)

    personlist = relationship('personlist', back_populates='minutesofmeeting')
    meeting = relationship('meeting', back_populates='minutesofmeeting')


    def __init__(self, author, date, description, attendee_list, invitee_list, follow_up_list,approver_list):
        self.author = author
        self.date = date
        self.description=description
        self.attendee_list=attendee_list
        self.invitee_list=invitee_list
        self.follow_up_list=follow_up_list
        self.approver_list=approver_list


    def __str__(self):
        return f"MinutesOfMeeting(Author : {self.author}, Date: {self.date}, Description: {self.description})"

