from fastapi import FastAPI
from src.main.meetingmanagement.controller.meeting_controller import router as meeting_router
from src.main.meetingmanagement.controller.minutesofmeeting_controller import router as minutesofmeeting_router
from src.main.meetingmanagement.controller.topic_controller import router as topic_router
from src.main.meetingmanagement.controller.projectlist_controller import  router as projectlist_router
from src.main.meetingmanagement.controller.personlist_controller import router as personlist_router
from src.main.meetingmanagement.controller.sectionlist_controller import router as sectionlist_router

app = FastAPI(title="Meeting Management API", version="1.0")

app.include_router(meeting_router)
app.include_router(minutesofmeeting_router)
app.include_router(topic_router)
app.include_router(projectlist_router)
app.include_router(personlist_router)
app.include_router(sectionlist_router)

@app.get("/")
def root():
    return {
        "service": "Meeting Management API",
        "status": "Running",
        "message": "Manage meetings, topics, minutes of meetings, personlists, and related projectlists through this API."
    }

