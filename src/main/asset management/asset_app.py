from fastapi import FastAPI
from src.main.asset_management.controller.asset_controller import route as asset_route

app = FastAPI(title="Asset Management API", version="1.0")
app.include_router(asset_route)

@app.get("/")
def root():
        return {"message": "Welcome to Asset Management API"}



