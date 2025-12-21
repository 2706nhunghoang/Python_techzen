from fastapi import HTTPException
from typing import List
from schemas.request.todo_schema import TodoCreate, TodoUpdate
from schemas.response.todo_schema import TodoOut

_todos = []
_id_counter = 1


class TodoService:
    @staticmethod
    def _find_todo_index(todo_id: int) -> int:
        for index, todo in enumerate(_todos):
            if todo["id"] == todo_id:
                return index
        raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")

    @staticmethod
    def _check_duplicate_title(title: str, exclude_id: int = None):
        for t in _todos:
            if t["title"].lower() == title.lower():
                if exclude_id is not None and t["id"] == exclude_id:
                    continue
                raise HTTPException(
                    status_code=409, detail=f"Todo title '{title}' already exists"
                )

    @staticmethod
    def create_todo(todo_in: TodoCreate) -> TodoOut:
        global _id_counter
        TodoService._check_duplicate_title(title=todo_in.title)

        new_todo = todo_in.model_dump()
        new_todo["id"] = _id_counter

        _todos.append(new_todo)
        _id_counter += 1
        return TodoOut(**new_todo)

    @staticmethod
    def get_todos(
            done: bool | None = None, keyword: str | None = None, limit: int = 10
    ) -> List[TodoOut]:

        filtered_list = [
            t
            for t in _todos
            if (done is None or t["done"] == done)
               and (keyword is None or keyword.lower() in t["title"].lower())
        ][:limit]

        return [TodoOut(**t) for t in filtered_list]

    @staticmethod
    def get_todo_by_id(todo_id: int) -> TodoOut | None:
        index = TodoService._find_todo_index(todo_id)
        return TodoOut(**_todos[index])

    @staticmethod
    def update_todo(todo_id: int, todo_in: TodoCreate) -> TodoOut | None:
        index = TodoService._find_todo_index(todo_id)
        TodoService._check_duplicate_title(title=todo_in.title, exclude_id=todo_id)

        updated_data = todo_in.model_dump()
        updated_data["id"] = todo_id

        _todos[index] = updated_data

        return TodoOut(**updated_data)

    @staticmethod
    def patch_todo(todo_id: int, todo_in: TodoUpdate) -> TodoOut | None:
        index = TodoService._find_todo_index(todo_id)
        if todo_in.title is not None:
            TodoService._check_duplicate_title(title=todo_in.title, exclude_id=todo_id)

        current_todo_data = _todos[index]
        update_data = todo_in.model_dump(exclude_unset=True)
        current_todo_data.update(update_data)

        return TodoOut(**current_todo_data)

    @staticmethod
    def delete_todo(todo_id: int) -> bool:
        index = TodoService._find_todo_index(todo_id)
        _todos.pop(index)
        return True
