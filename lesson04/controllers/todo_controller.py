from fastapi import APIRouter, HTTPException, Query, status, Response
from typing import List, Optional

from schemas.request.todo_schema import TodoCreate, TodoUpdate
from schemas.response.todo_schema import TodoOut
from services.todo_service import TodoService

todo_router = APIRouter(prefix="/todos", tags=["Todos"])


@todo_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new Todo",
    description="Tạo một todo mới. Title không được trùng nhau.",
    response_model=TodoOut,
    responses={
        409: {"description": "Conflict - Title already exists"},
        422: {"description": "Validation Error - Invalid data"},
    },
)
def create_todo(todo: TodoCreate):
    return TodoService.create_todo(todo)


@todo_router.get(
    "/",
    response_model=List[TodoOut],
    summary="Get list of Todos",
    description="Lấy danh sách các công việc. Hỗ trợ lọc theo trạng thái (done), tìm kiếm từ khóa (keyword) theo title và giới hạn kết quả (limit).",
)
def get_todos(
        done: bool | None = None,
        keyword: str | None = None,
        limit: int = Query(10, ge=1, le=50),
):
    return TodoService.get_todos(done, keyword, limit)


@todo_router.get(
    "/{todo_id}",
    response_model=TodoOut,
    summary="Get a specific Todo",
    description="Lấy thông tin chi tiết một công việc theo ID.",
    responses={
        404: {"description": "Not found - ID không tồn tại"},
    },
)
def get_todo_detail(todo_id: int):
    todo = TodoService.get_todo_by_id(todo_id)
    return todo


@todo_router.put(
    "/{todo_id}",
    response_model=TodoOut,
    summary="Update full Todo",
    description="Cập nhật toàn bộ thông tin Todo (trừ ID). Bắt buộc phải gửi đủ dữ liệu như lúc tạo mới.",
    responses={
        404: {"description": "Not found - ID không tồn tại"},
        409: {"description": "Conflict - Title already exists"},
        422: {"description": "Validation Error - Invalid data"},
    },
)
def update_full_todo(todo_id: int, todo: TodoCreate):
    updated_todo = TodoService.update_todo(todo_id, todo)
    return updated_todo


@todo_router.patch(
    "/{todo_id}",
    response_model=TodoOut,
    summary="Update partial Todo",
    description="Chỉ cập nhật các trường được gửi lên (các trường khác giữ nguyên).",
    responses={
        404: {"description": "Not found - ID không tồn tại"},
        409: {"description": "Conflict - Title already exists"},
    },
)
def update_partial_todo(todo_id: int, todo: TodoUpdate):
    updated_todo = TodoService.patch_todo(todo_id, todo)
    return updated_todo


@todo_router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Todo",
    description="Xóa vĩnh viễn một Todo.",
    responses={404: {"description": "Not found - ID không tồn tại"}},
)
def delete_todo(todo_id: int):
    TodoService.delete_todo(todo_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
