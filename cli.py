# cli.py
from database import session
from models import TaskManager, Task

def list_tasks():
    tasks = session.query(Task).all()
    for task in tasks:
        print(f"{task.id}. {task.title} | Completed: {task.completed}")

def add_task():
    title = input("Task Title: ")
    description = input("Task Description: ")
    manager_id = int(input("Manager ID: "))
    task = Task(title=title, description=description, task_manager_id=manager_id)
    session.add(task)
    session.commit()
    print("Task added.")

def complete_task():
    task_id = int(input("Enter Task ID to mark complete: "))
    task = session.query(Task).get(task_id)
    if task:
        task.completed = True
        session.commit()
        print("Task marked as complete.")
    else:
        print("Task not found.")

def main():
    while True:
        print("\nTASK MANAGER CLI")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
