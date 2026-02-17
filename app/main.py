from fastapi import FastAPI
from app.routers.tasks import router as tasks_router

# NEW IMPORTS
from app.db import engine, Base
from app.orm_models import TaskORM  # noqa

app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    description="A simple Task Manager REST API (FastAPI) for internship portfolio.",
)

# CREATE TABLES
Base.metadata.create_all(bind=engine)

app.include_router(tasks_router)


@app.get("/")
def root():
    return {"message": "Task Manager API is running. Go to /docs"}
