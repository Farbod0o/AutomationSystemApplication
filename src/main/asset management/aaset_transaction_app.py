from fastapi import FastAPI
from src.main.asset_management.controller.asset_transection_controller import route as asset_transection_route

app = FastAPI(title="Asset Transection App",version="1.0")
app.include_router(asset_transection_route)

@app.get("/")
def root():
    return {"message": "welcome to Asset Transection App"}
