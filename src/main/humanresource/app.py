from fastapi import FastAPI
from src.main.humanresource.controller.work_shift_controller import router as work_shift_router


app = FastAPI(title="Work Shift Management API", version="1.0")

app.include_router(work_shift_router)


@app.get("/")
def root():
    return {"message": "Welcome"}
