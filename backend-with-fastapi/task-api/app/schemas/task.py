"""Pydantic schemas for Task resource — separate from ORM model."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.task import TaskStatus


class TaskBase(BaseModel):
    """Fields shared by create and read schemas."""

    title: str = Field(..., min_length=1, max_length=200, examples=["Learn FastAPI"])
    description: str | None = Field(default=None, max_length=2000)
    status: TaskStatus = Field(default=TaskStatus.PENDING)


class TaskCreate(TaskBase):
    """Request body for POST /tasks."""

    pass


class TaskUpdate(BaseModel):
    """Request body for PATCH /tasks/{id} — all fields optional."""

    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    status: TaskStatus | None = Field(default=None)


class TaskRead(TaskBase):
    """Response schema for Task resource."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class TaskListResponse(BaseModel):
    """Paginated list of tasks."""

    items: list[TaskRead]
    total: int
    skip: int
    limit: int
