from sqlalchemy import select
from sqlalchemy.orm import Session
from models.todo import Todo
from repositories.base_repository import BaseRepository


class TodoRepository(BaseRepository[Todo]):
    def __init__(self):
        super().__init__(Todo)

    def get_by_title(self, db: Session, title: str) -> Todo | None:
        stmt = select(Todo).where(Todo.title.ilike(title))
        return db.execute(stmt).scalars().first()

    def search(
        self,
        db: Session,
        *,
        done: bool = None,
        keyword: str = None,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Todo]:
        stmt = select(Todo)
        if done is not None:
            stmt = stmt.where(Todo.done == done)
        if keyword:
            stmt = stmt.where(Todo.title.ilike(f"%{keyword}%"))
        return list(db.execute(stmt.offset(offset).limit(limit)).scalars().all())
