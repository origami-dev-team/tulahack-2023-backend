from pydantic import BaseModel, Field
from datetime import datetime
from utils import id, now
from typing import List


class User(BaseModel):
    id: str = Field(default_factory=id)
    username: str
    totalLikes: int = Field(default=0)
    comics: List[str] = []
    created_at: datetime = Field(default_factory=now)
    updated_at: datetime = Field(default_factory=now)
