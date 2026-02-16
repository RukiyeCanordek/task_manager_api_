from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional

from app.models import Task, TaskCreate, TaskUpdate
from app.storage import load_tasks, save_tasks, next_id, find_task, now_iso

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=List[Task])
def list_tasks(
    status: Optional[str] = Query(default=None, description="all|done|pending"),
    q: Optional[str] = Query(default=None, description="search in title/description"),
):
    tasks = load_tasks()

    if status in ("done", "pending"):
        want_done = status == "done"
        tasks = [t for t in tasks if bool(t.get("completed")) == want_done]
    elif status not in (None, "all"):
        raise HTTPException(status_code=400, detail="status must be one of: all, done, pending")

    if q:
        qq = q.lower()
        tasks = [
            t for t in tasks
            if qq in (t.get("title") or "").lower()
            or qq in (t.get("description") or "").lower()
        ]

    return tasks


@router.post("", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    tasks = load_tasks()
    now = now_iso()

    task = {
        "id": next_id(tasks),
        "title": payload.title,
        "description": payload.description,
        "completed": False,
        "created_at": now,
        "updated_at": now,
    }

    tasks.append(task)
    save_tasks(tasks)
    return task


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title is not None:
        task["title"] = payload.title
    if payload.description is not None:
        task["description"] = payload.description
    if payload.completed is not None:
        task["completed"] = payload.completed

    task["updated_at"] = now_iso()
    save_tasks(tasks)
    return task


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return None
