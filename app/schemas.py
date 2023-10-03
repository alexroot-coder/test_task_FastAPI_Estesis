import uuid
from pydantic import BaseModel


class Task(BaseModel):
    task_uuid: uuid.UUID


class TaskPreview(Task):
    description: str
    params: dict


class TaskUpdate(BaseModel):
    description: str
    params: dict


class TaskAdd(BaseModel):
    description: str
    params: dict
