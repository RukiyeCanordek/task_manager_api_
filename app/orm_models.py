from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class TaskORM(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, nullable=False, default=False)
    created_at = Column(String, nullable=False)  # ISO string
    updated_at = Column(String, nullable=False)  # ISO string
