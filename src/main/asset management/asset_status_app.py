from fastapi import FastAPI
from src.main.asset_management.controller.asset_status_controller import route as asset_status_route

app = FastAPI(title="Asset Status App", version="1.0")
app.include_router(asset_status_route)


@app.get("/")
def root():
    return {"message": "Welcome to Asset Status App"}
