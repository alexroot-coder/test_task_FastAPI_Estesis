import uuid
from sqlalchemy.orm import Session
from app import models, schemas


def get_tasks(db: Session):
    return db.query(models.Task).all()


def update_task(db: Session, task_uuid: uuid.UUID, task):
    tmp_task = db.query(models.Task).filter(models.Task.task_uuid == task_uuid).first()
    tmp_task.description = task.description
    tmp_task.params = task.params
    db.add(tmp_task)
    db.commit()
    db.refresh(tmp_task)
    return tmp_task


def create_task(db: Session, task: schemas.TaskAdd):
    db_item = models.Task(**task.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
