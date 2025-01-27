from fastapi import FastAPI
from src.main.ticket_status_controller import router as ticket_status_router

app = FastAPI(title="Ticket Status Management API", version="1.0")

app.include_router(ticket_status_router)


@app.get("/")
def root():
    return {"message": "Welcome to Ticket Status Management API"}
