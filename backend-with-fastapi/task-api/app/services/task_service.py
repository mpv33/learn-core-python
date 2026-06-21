"""Task service — database operations with ownership and RBAC rules."""

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.exceptions import ForbiddenError, NotFoundError
from app.core.rbac import is_admin
from app.models.task import Task, TaskStatus
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    """Encapsulates task CRUD with owner-scoped access for regular users."""

    def __init__(self, db: Session, current_user: User) -> None:
        self.db = db
        self.current_user = current_user

    def _base_query(self):
        """Scope query to current user's tasks unless admin."""
        query = select(Task)
        if not is_admin(self.current_user):
            query = query.where(Task.owner_id == self.current_user.id)
        return query

    def _ensure_access(self, task: Task) -> None:
        """Raise ForbiddenError if user cannot access this task."""
        if not is_admin(self.current_user) and task.owner_id != self.current_user.id:
            raise ForbiddenError("You do not have access to this task")

    def list_tasks(
        self,
        *,
        status: TaskStatus | None = None,
        skip: int = 0,
        limit: int = 100,
    ) -> tuple[list[Task], int]:
        query = self._base_query()
        count_query = select(func.count()).select_from(Task)
        if not is_admin(self.current_user):
            count_query = count_query.where(Task.owner_id == self.current_user.id)

        if status is not None:
            query = query.where(Task.status == status)
            count_query = count_query.where(Task.status == status)

        total = self.db.scalar(count_query) or 0
        tasks = self.db.scalars(
            query.order_by(Task.created_at.desc()).offset(skip).limit(limit)
        ).all()
        return list(tasks), total

    def get_task(self, task_id: int) -> Task:
        task = self.db.get(Task, task_id)
        if task is None:
            raise NotFoundError(f"Task {task_id} not found")
        self._ensure_access(task)
        return task

    def create_task(self, payload: TaskCreate) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            owner_id=self.current_user.id,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, payload: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        updates = payload.model_dump(exclude_unset=True)
        for field, value in updates.items():
            setattr(task, field, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        self.db.delete(task)
        self.db.commit()
