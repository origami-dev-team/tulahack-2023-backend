from enum import Enum

class Collection(str, Enum):
    Sprite = "sprite"

class SpriteCategory(str, Enum):
    Character = "character"
    Background = "background"
    