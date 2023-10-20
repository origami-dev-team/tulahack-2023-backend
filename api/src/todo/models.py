from pydantic import BaseModel, Field
from datetime import datetime
from utils import id, now


class Todo(BaseModel):
    id: str = Field(default_factory=id)
    title: str
    description: str | None = Field(default=None)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=now)
    updated_at: datetime = Field(default_factory=now)


class CreateTodoDTO(BaseModel):
    title: str
    description: str | None = Field(default=None)


class UpdateTodoDTO(BaseModel):
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    completed: bool | None = Field(default=None)
