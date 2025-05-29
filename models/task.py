# models/task.py
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    completed = Column(Boolean, default=False)

    task_manager_id = Column(Integer, ForeignKey('task_managers.id'))
    task_manager = relationship("TaskManager", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"
