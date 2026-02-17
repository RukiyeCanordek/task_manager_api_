from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models import Task, TaskCreate, TaskUpdate
from app.db import get_db
from app.orm_models import TaskORM
from app.storage import now_iso

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=List[Task])
def list_tasks(
    status: Optional[str] = Query(default=None, description="all|done|pending"),
    q: Optional[str] = Query(default=None, description="search in title/description"),
    db: Session = Depends(get_db),
):
    query = db.query(TaskORM)

    if status in ("done", "pending"):
        want_done = status == "done"
        query = query.filter(TaskORM.completed == want_done)
    elif status not in (None, "all"):
        raise HTTPException(status_code=400, detail="status must be one of: all, done, pending")

    if q:
        qq = f"%{q}%"
        query = query.filter(
            (TaskORM.title.ilike(qq)) |
            (TaskORM.description.ilike(qq))
        )

    tasks = query.order_by(TaskORM.id.desc()).all()
    return [Task(**t.__dict__) for t in tasks]


@router.post("", response_model=Task, status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    now = now_iso()
    task = TaskORM(
        title=payload.title,
        description=payload.description,
        completed=False,
        created_at=now,
        updated_at=now,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task.__dict__


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskORM).filter(TaskORM.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task.__dict__


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(TaskORM).filter(TaskORM.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title is not None:
        task.title = payload.title
    if payload.description is not None:
        task.description = payload.description
    if payload.completed is not None:
        task.completed = payload.completed

    task.updated_at = now_iso()
    db.commit()
    db.refresh(task)
    return task.__dict__


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskORM).filter(TaskORM.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return None
