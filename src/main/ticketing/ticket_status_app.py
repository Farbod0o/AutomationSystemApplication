from fastapi import FastAPI
from src.main.ticketing.controller.ticket_status_controller import route as ticket_status_route

app = FastAPI(title="Ticket Status Management API", version="1.0")

app.include_route(ticket_status_route)


@app.get("/")
def root():
    return {"message": "Welcome to Ticket Status Management API"}
