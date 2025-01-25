from fastapi import FastAPI
from src.main.message.controller import route as message_route

app = FastAPI(title="Message Management API", version="1.0")

app.include_router(message_route)

@app.get("/")
def root():
    return {"message": "Welcome to Message Management API"}
