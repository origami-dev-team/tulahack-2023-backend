from fastapi import FastAPI
from todo.router import router as todo_router
from user.router import router as user_router

app = FastAPI()

app.include_router(todo_router, prefix="/todo")
app.include_router(user_router, prefix="/auth")
