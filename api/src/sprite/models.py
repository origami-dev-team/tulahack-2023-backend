from pydantic import BaseModel, Field
from constants import SpriteCategory
from datetime import datetime
from utils import now


class Sprite(BaseModel):
    id: str
    category: SpriteCategory
    url: str
    created_at: datetime = Field(default_factory=now)