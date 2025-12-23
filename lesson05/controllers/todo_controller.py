from fastapi import APIRouter, Depends, Query, status, Response
from sqlalchemy.orm import Session
from typing import List

from dependencies.db import get_db
from schemas.request.todo_schema import TodoCreate, TodoUpdate
from schemas.response.todo_schema import TodoOut
from schemas.response.base import SuccessResponse, ErrorSchema
from services.todo_service import TodoService

todo_router = APIRouter(prefix="/todos", tags=["Todos"])
service = TodoService()


@todo_router.get(
    "",
    response_model=SuccessResponse[List[TodoOut]],
    summary="Get list of Todos",
    responses={
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
def get_todos(
    done: bool | None = None,
    keyword: str | None = None,
    offset: int = 0,
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    todos = service.search_todos(
        db, done=done, keyword=keyword, offset=offset, limit=limit
    )
    data = [TodoOut.model_validate(t) for t in todos]
    return SuccessResponse(data=data)


@todo_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse[TodoOut],
    summary="Create a new Todo",
    responses={
        409: {"model": ErrorSchema, "description": "Conflict - Duplicate title"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = service.create_todo(db, todo)
    return SuccessResponse(data=TodoOut.model_validate(new_todo))


@todo_router.get(
    "/{todo_id:int}",
    response_model=SuccessResponse[TodoOut],
    summary="Get a specific Todo",
    responses={
        404: {"model": ErrorSchema, "description": "Not Found - ID does not exist"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
def get_todo_detail(todo_id: int, db: Session = Depends(get_db)):
    todo = service.get_todo(db, todo_id)
    return SuccessResponse(data=TodoOut.model_validate(todo))


@todo_router.patch(
    "/{todo_id:int}",
    response_model=SuccessResponse[TodoOut],
    summary="Update partial Todo",
    responses={
        404: {"model": ErrorSchema, "description": "Not Found - ID does not exist"},
        409: {"model": ErrorSchema, "description": "Conflict - Duplicate title"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
def update_partial_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = service.update_todo_patch(db, todo_id, todo)
    return SuccessResponse(data=TodoOut.model_validate(updated_todo))


@todo_router.delete(
    "/{todo_id:int}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Todo",
    responses={
        404: {"model": ErrorSchema, "description": "Not Found - ID does not exist"},
        422: {"model": ErrorSchema, "description": "Validation Error"},
    },
)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    service.delete_todo(db, todo_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
