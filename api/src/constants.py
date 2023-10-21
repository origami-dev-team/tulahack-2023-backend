from os import getenv
from enum import Enum

TUNNEL_HOST = getenv("TUNNEL_HOST")
TUNNEL_PORT = getenv("TUNNEL_PORT")
TUNNEL_URL = f"http://{TUNNEL_HOST}:{TUNNEL_PORT}"
BUCKET_NAME = "sandbox-98197.appspot.com"

class Collection(str, Enum):
    Sprite = "sprite"

class SpriteCategory(str, Enum):
    Character = "character"
    Background = "background"
    