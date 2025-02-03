from sqlalchemy import Column, Integer, String, Date, column
from src.main.database.da import Base


class MinutesOfMetting(Base):
    __tablename__ = 'Minutes_Of_Metting'
    id = Column(Integer, primary_key=True)
    author = Column("author",String(30),nullabel=False)
    date = Column("date",Date,nullabel=False)
    description = Column("description",String(255),nullable=True)
    attendee_list=Column("attendee_list",String(255),nullable=True)
    invitee_list=Column("invitee_list",String(255),nullable=True)
    follow_up_list=Column("follow_up_list",String(255),nullable=True)
    approver_list=Column("approver_list",String(255),nullable=True)


    def __init__(self, author, date, description, attendee_list, invitee_list, follow_up_list):
        self.author = author
        self.date = date
        self.description=description
        self.attendee_list=attendee_list
        self.invitee_list=invitee_list
        self.follow_up_list=follow_up_list


    def __str__(self):
        return f"MinutesOfMeeting(Author : {self.author}, Date: {self.date}, Description: {self.description})"

