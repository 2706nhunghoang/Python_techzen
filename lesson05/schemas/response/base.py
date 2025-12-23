# schemas/response/base.py

from typing import Generic, TypeVar
from pydantic import BaseModel, Field
from core.trace import trace_id_ctx

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T
    message: str | None = None
    trace_id: str | None = None


class ErrorSchema(BaseModel):
    success: bool = False
    message: str = Field(..., description="Nội dung thông báo lỗi cụ thể")
    trace_id: str | None = Field(default_factory=lambda: trace_id_ctx.get())
