from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=3, description="Tiêu đề công việc")
    description: str | None = None
    priority: int = Field(..., ge=1, le=5, description="Độ ưu tiên 1-5")
    done: bool = False


class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=3)
    description: str | None = None
    priority: int | None = Field(None, ge=1, le=5)
    done: bool | None = None
