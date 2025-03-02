# view_tasks.py
from task_scheduler import TaskScheduler

def view_tasks(scheduler):
    tasks = scheduler.view_tasks()
    print("\nCurrent Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task.title} - {task.description} - {task.priority} - {task.deadline}")
