import uuid
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import engine, get_db, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.put("/tasks/{task_uuid}", response_model=schemas.Task)
def update_task(task_uuid: uuid.UUID = None, task: schemas.TaskUpdate = None, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_uuid=task_uuid, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.post("/tasks/add", response_model=schemas.Task)
def add_task(task: schemas.TaskAdd, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@app.get("/tasks", response_model=list[schemas.TaskPreview])
def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return tasks
