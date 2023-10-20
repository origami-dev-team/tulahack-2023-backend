from .models import CreateSpriteDTO, Sprite
from constants import SpriteCategory, Collection
from fastapi import APIRouter
from typing import List
from database import firestore

router = APIRouter()


@router.get("/")
async def get_all() -> List[Sprite]:
    all = await firestore.get_all(collection=Collection.Sprite)
    return [Sprite(**one) for one in all]

@router.get("/{category}")
async def get_all_by_category(category: SpriteCategory) -> List[Sprite]:
    all = await firestore.get_all(collection=Collection.Sprite)
    all = [Sprite(**one) for one in all]
    return [one for one in all if one.category == category]

@router.post("/")
async def create(create_sprite_dto: CreateSpriteDTO) -> Sprite:
    sprite = Sprite(**create_sprite_dto.model_dump())
    sprite = await firestore.create(collection=Collection.Sprite, data=sprite.model_dump())
    return Sprite(**sprite)

