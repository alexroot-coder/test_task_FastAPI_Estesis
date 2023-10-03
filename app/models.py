import uuid
from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    task_uuid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    description = Column(String, index=True, nullable=False)
    params = Column(JSON)
