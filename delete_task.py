# delete_task.py
from task_scheduler import TaskScheduler

def delete_task(scheduler):
    tasks = scheduler.view_tasks()
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task.title} - {task.description} - {task.priority} - {task.deadline}")

    index = int(input("Enter task number to delete: ")) - 1
    scheduler.delete_task(index)
    print("Task deleted successfully.")
