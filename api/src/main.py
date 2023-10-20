from fastapi import FastAPI
from fastapi import FastAPI
from todo.router import router as todo_router

app = FastAPI()

app.include_router(todo_router, prefix="/todo")
