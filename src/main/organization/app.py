from fastapi import FastAPI
from src.main.organization.controller.organization_controller import router as organization_router
from src.main.organization.controller.department_controller import router as department_router
from src.main.organization.controller.section_controller import router as section_router

app = FastAPI(title="Organization Management API", version="1.0")

app.include_router(organization_router)
app.include_router(department_router)
app.include_router(section_router)

@app.get("/")
def root():
    return {
        "service": "Organization System",
        "status": "Active",
        "description": "Use this API to organizations, departments, organizations, and sections."
    }

