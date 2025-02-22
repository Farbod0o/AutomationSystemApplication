from fastapi import FastAPI
from src.main.ticketing.controller.ticket_controller import route as ticket_route

app = FastAPI(title="Ticket Management API", version="1.0")

app.include_route(ticket_route)


@app.get("/")
def root():
    return {"message": "Welcome to Ticket Management API"}
