"""Task CRUD endpoints — requires authentication; RBAC enforced in service layer."""

from fastapi import APIRouter, Depends, Query, status

from app.api.deps import get_task_service, require_permission
from app.core.rbac import Permission
from app.models.task import TaskStatus
from app.models.user import User
from app.schemas.task import TaskCreate, TaskListResponse, TaskRead, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=TaskListResponse)
def list_tasks(
    _user: User = Depends(require_permission(Permission.TASK_READ)),
    status: TaskStatus | None = Query(default=None, description="Filter by status"),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    service: TaskService = Depends(get_task_service),
) -> TaskListResponse:
    """List tasks (own tasks for users; all tasks for admin)."""
    tasks, total = service.list_tasks(status=status, skip=skip, limit=limit)
    return TaskListResponse(items=tasks, total=total, skip=skip, limit=limit)


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    _user: User = Depends(require_permission(Permission.TASK_WRITE)),
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    """Create a new task owned by the current user."""
    return service.create_task(payload)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: int,
    _user: User = Depends(require_permission(Permission.TASK_READ)),
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    """Get a single task by ID."""
    return service.get_task(task_id)


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    _user: User = Depends(require_permission(Permission.TASK_WRITE)),
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    """Partially update a task."""
    return service.update_task(task_id, payload)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    _user: User = Depends(require_permission(Permission.TASK_DELETE)),
    service: TaskService = Depends(get_task_service),
) -> None:
    """Delete a task."""
    service.delete_task(task_id)
