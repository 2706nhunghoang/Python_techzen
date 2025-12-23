from sqlalchemy.orm import Session

from core.exceptions import AppException
from models.todo import Todo
from repositories.todo_repository import TodoRepository
from schemas.request.todo_schema import TodoCreate, TodoUpdate


class TodoService:
    def __init__(self):
        self.repo = TodoRepository()

    def get_todo(self, db: Session, todo_id: int) -> Todo:
        todo = self.repo.get_by_id(db, todo_id)
        if not todo:
            raise AppException(
                status_code=404, message=f"Todo with ID {todo_id} not found"
            )
        return todo

    def create_todo(self, db: Session, data: TodoCreate) -> Todo:
        existed = self.repo.get_by_title(db, data.title)
        if existed:
            raise AppException(status_code=409, message="Title already exists")

        todo = Todo(**data.model_dump())
        return self.repo.create(db, todo)

    def search_todos(
            self,
            db: Session,
            done: bool | None = None,
            keyword: str | None = None,
            offset: int = 0,
            limit: int = 100,
    ) -> list[Todo]:
        return self.repo.search(
            db, done=done, keyword=keyword, offset=offset, limit=limit
        )

    def update_todo_put(self, db: Session, todo_id: int, data: TodoCreate) -> Todo:
        todo = self.get_todo(db, todo_id)

        existed = self.repo.get_by_title(db, data.title)
        if existed and existed.id != todo_id:
            raise AppException(status_code=409, message="Title already exists")

        update_data = data.model_dump()
        return self.repo.update(db, todo, update_data)

    def update_todo_patch(self, db: Session, todo_id: int, data: TodoUpdate) -> Todo:
        todo = self.get_todo(db, todo_id)

        if data.title:
            existed = self.repo.get_by_title(db, data.title)
            if existed and existed.id != todo_id:
                raise AppException(status_code=409, message="Title already exists")

        update_data = data.model_dump(exclude_unset=True)
        return self.repo.update(db, todo, update_data)

    def delete_todo(self, db: Session, todo_id: int) -> None:
        todo = self.get_todo(db, todo_id)
        self.repo.delete(db, todo)
