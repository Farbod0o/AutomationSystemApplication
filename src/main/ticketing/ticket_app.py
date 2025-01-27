from fastapi import FastAPI
from src.main.ticket.controller import router as ticket_router

app = FastAPI(title="Ticket Management API", version="1.0")

app.include_router(ticket_router)


@app.get("/")
def root():
    return {"message": "Welcome to Ticket Management API"}
