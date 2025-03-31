from fastapi import FastAPI
from src.main.organization.controller.section_controller import router as section_router


app = FastAPI(title="Section Management API", version="1.0")

app.include_router(section_router)

@app.get("/")
def root():
    return {"message": "Welcome to Section Management API"}