# task.py
class Task:
    def __init__(self, title, description, priority, deadline):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'deadline': self.deadline
        }
