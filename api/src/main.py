from fastapi import FastAPI
from sprite.router import router as sprite_router
from user.router import router as user_router
from constants import Collection
from todo.router import router as todo_router

app = FastAPI()

app.include_router(todo_router, prefix="/todo")
app.include_router(user_router, prefix="/auth")
app.include_router(sprite_router, prefix=f"/{Collection.Sprite}")
