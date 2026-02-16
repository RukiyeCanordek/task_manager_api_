import json
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

DATA_PATH = Path("data/tasks.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_tasks() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_PATH.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def next_id(tasks: List[Dict[str, Any]]) -> int:
    return (max(t["id"] for t in tasks) + 1) if tasks else 1


def find_task(tasks: List[Dict[str, Any]], task_id: int) -> Optional[Dict[str, Any]]:
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None
