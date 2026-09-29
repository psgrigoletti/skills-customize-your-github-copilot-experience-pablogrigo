from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    completed: bool


tasks = [
    {"id": 1, "title": "Read the API guide", "completed": False},
    {"id": 2, "title": "Build a first endpoint", "completed": True},
]