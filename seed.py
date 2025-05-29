# seed.py
from database import Base, engine, session
from models import TaskManager, Task

# Recreate the DB
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Add sample TaskManager
manager = TaskManager(name="Alice", email="alice@example.com")
session.add(manager)
session.commit()

# Add sample Tasks
task1 = Task(title="Buy groceries", description="Milk, Eggs, Bread", completed=False, task_manager=manager)
task2 = Task(title="Finish project", description="Phase 3 CLI app", completed=False, task_manager=manager)

session.add_all([task1, task2])
session.commit()

print("Seeded database.")
