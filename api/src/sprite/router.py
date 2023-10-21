import requests
from .models import Sprite, GenerateSpriteDTO
from constants import SpriteCategory, Collection
from fastapi import APIRouter
from typing import List
from database import firestore
from fastapi import UploadFile
from utils import id
from constants import TUNNEL_URL

router = APIRouter()


@router.get("/{category}")
async def get_all(category: SpriteCategory) -> List[str]:
    all = await firestore.get_all(collection=Collection.Sprite)
    sprites = [Sprite(**one) for one in all if one["category"] == category]
    urls = [sprite.url for sprite in sprites]
    return urls

@router.post("/{category}")
async def upload(category: SpriteCategory, file: UploadFile) -> Sprite:
    file_id = id()
    url = await firestore.upload_file(file=file, folder=category, id=file_id)
    sprite = Sprite(id=file_id, category=category, url=url)
    sprite = await firestore.create(collection=Collection.Sprite, data=sprite.model_dump())
    return Sprite(**sprite)

@router.post("/generate/")
async def generate(generateSpriteDTO: GenerateSpriteDTO) -> str:
    print(generateSpriteDTO)
    hello = requests.get(f"{TUNNEL_URL}/hello/").json()
    return hello