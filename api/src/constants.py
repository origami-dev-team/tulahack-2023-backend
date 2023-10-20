from enum import Enum

BUCKET_NAME = "sandbox-98197.appspot.com"

class Collection(str, Enum):
    Sprite = "sprite"

class SpriteCategory(str, Enum):
    Character = "character"
    Background = "background"
    