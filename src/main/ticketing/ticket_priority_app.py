from fastapi import FastAPI
from src.main.ticketing.controller.ticket_priority_controller import route as ticket_priority_route

app = FastAPI(title="Priority Management API", version="1.0")

app.include_router(ticket_priority_route)

@app.get("/")
def root():
     return {"message": "Welcome to Priority Management API"}


