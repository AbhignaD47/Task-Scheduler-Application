# task_scheduler.py
import json
from task import Task

class TaskScheduler:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def add_task(self, title, description, priority, deadline):
        task = Task(title, description, priority, deadline)
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, index, title=None, description=None, priority=None, deadline=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if priority:
                self.tasks[index].priority = priority
            if deadline:
                self.tasks[index].deadline = deadline
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def view_tasks(self):
        return sorted(self.tasks, key=lambda t: (t.priority, t.deadline))
