from pydantic import BaseModel, Field
from utils import id
from constants import SpriteCategory


class Sprite(BaseModel):
    id: str = Field(default_factory=id)
    category: SpriteCategory
    url: str
    
class CreateSpriteDTO(BaseModel):
    category: SpriteCategory
    url: str
