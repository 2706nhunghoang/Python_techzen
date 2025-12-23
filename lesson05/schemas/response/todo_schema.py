from pydantic import BaseModel


class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    priority: int
    done: bool

    class Config:
        from_attributes = True
