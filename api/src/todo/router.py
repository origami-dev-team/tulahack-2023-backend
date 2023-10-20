from .models import Todo, CreateTodoDTO, UpdateTodoDTO
from fastapi import APIRouter
from typing import List
from database import firestore
from utils import now

router = APIRouter()


@router.get("/")
async def get_all() -> List[Todo]:
    all = await firestore.get_all(collection="Todo")
    return [Todo(**one) for one in all]


@router.post("/")
async def create(create_todo_dto: CreateTodoDTO) -> Todo:
    todo = Todo(**create_todo_dto.model_dump())
    todo = await firestore.create(collection="Todo", data=todo.model_dump())
    return Todo(**todo)


@router.put("/{id}")
async def update(id: str, update_todo_dto: UpdateTodoDTO) -> Todo:
    todo = await firestore.update(
        collection="Todo",
        data=update_todo_dto.model_dump() | {"updated_at": now()},
        id=id,
    )
    return Todo(**todo)
