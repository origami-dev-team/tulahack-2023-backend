from fastapi import FastAPI
from fastapi import FastAPI
from sprite.router import router as sprite_router
from constants import Collection

app = FastAPI()

app.include_router(sprite_router, prefix=f"/{Collection.Sprite}")
