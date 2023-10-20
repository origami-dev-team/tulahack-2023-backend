from user.models import User
from fastapi import APIRouter
from typing import List
from database import firestore
from utils import now

router = APIRouter()


@router.post("/")
async def create(username: str) -> User:
    user = User(username=username)
    print(user)
    user = await firestore.create(collection="User", data=user.model_dump())
    return User(**user)
