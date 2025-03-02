# edit_task.py
from task_scheduler import TaskScheduler
from utils import validate_priority, validate_date

def edit_task(scheduler):
    tasks = scheduler.view_tasks()
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task.title} - {task.description} - {task.priority} - {task.deadline}")

    index = int(input("Enter task number to edit: ")) - 1
    title = input("Enter new title (leave blank to keep current): ")
    description = input("Enter new description (leave blank to keep current): ")
    priority = input("Enter new priority (leave blank to keep current): ")
    deadline = input("Enter new deadline (leave blank to keep current): ")

    try:
        if priority:
            validate_priority(priority)
        if deadline:
            validate_date(deadline)
        scheduler.edit_task(index, title or None, description or None, priority or None, deadline or None)
        print("Task edited successfully.")
    except ValueError as e:
        print(e)
