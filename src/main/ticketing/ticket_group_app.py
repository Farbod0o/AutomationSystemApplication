from fastapi import FastAPI
from src.main.ticketing.controller.ticket_group_controller import route as ticket_group_route

app = FastAPI(title="Ticket Group Management API", version="1.0")

app.include_router(ticket_group_router)


@app.get("/")
def root():
    return {"message": "Welcome to Ticket Group Management API"}
