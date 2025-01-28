from fastapi import FastAPI
from src.main.ticketing.controller.message_controller import route as message_route

app = FastAPI(title="Message Management API", version="1.0")

app.include_router(message_route)

@app.get("/")
def root():
    return {"message": "welcome to Message Management API"}
