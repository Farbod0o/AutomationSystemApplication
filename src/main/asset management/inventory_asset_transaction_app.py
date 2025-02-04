from fastapi import FastAPI
from src.main.asset_management.controller.inventory_asset_transection_controller import route as inventory_asset_transection_route

app = FastAPI(title="Inventory Asset Transection App", version="1.0")
app.include_router(inventory_asset_transection_route)


@app.get("/")
def root():
    return {"message": "Welcome to Inventory Asset Transection App"}
