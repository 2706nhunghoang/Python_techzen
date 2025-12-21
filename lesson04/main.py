import uvicorn
from fastapi import FastAPI
from controllers import todo_controller

app = FastAPI()

app.include_router(todo_controller.todo_router)


@app.get("/")
def root():
    return {"message": "Welcome to Todo API"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
