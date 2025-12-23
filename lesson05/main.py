import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from controllers import todo_controller
from core.exception_handlers import app_exception_handler, validation_exception_handler
from core.exceptions import AppException
from core.middlewares.db_session import DBSessionMiddleware
from core.middlewares.trace_id import TraceIdMiddleware

app = FastAPI()

app.include_router(todo_controller.todo_router)

__MIDDLEWARES__ = [DBSessionMiddleware, TraceIdMiddleware]
for middleware in __MIDDLEWARES__:
    app.add_middleware(middleware)

__EXCEPTION_HANDLERS__ = [
    (AppException, app_exception_handler),
    (RequestValidationError, validation_exception_handler),
]
for exc, handler in __EXCEPTION_HANDLERS__:
    app.add_exception_handler(exc, handler)


@app.get("/")
def root():
    return {"message": "Welcome to Todo API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
