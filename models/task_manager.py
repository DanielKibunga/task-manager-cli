# models/task_manager.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class TaskManager(Base):
    __tablename__ = 'task_managers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    tasks = relationship("Task", back_populates="task_manager")

    def __repr__(self):
        return f"<TaskManager(id={self.id}, name='{self.name}')>"
