# add_task.py
from task_scheduler import TaskScheduler
from utils import validate_priority, validate_date

def add_task(scheduler):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (High, Medium, Low): ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")

    try:
        validate_priority(priority)
        validate_date(deadline)
        scheduler.add_task(title, description, priority, deadline)
        print("Task added successfully.")
    except ValueError as e:
        print(e)
