from fastapi import FastAPI
from src.main.asset_management.controller.asset_room_controller import route as asset_room_route

app = FastAPI(title="Asset Transection App", version="1.0")
app.include_router(asset_room_route)


@app.get("/")
def root():
    return {"message": "Welcome to Asset Room App"}
