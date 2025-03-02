# main.py
from task_scheduler import TaskScheduler
from add_task import add_task
from edit_task import edit_task
from delete_task import delete_task
from view_tasks import view_tasks

def main():
    scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(scheduler)
        elif choice == '2':
            edit_task(scheduler)
        elif choice == '3':
            delete_task(scheduler)
        elif choice == '4':
            view_tasks(scheduler)
        elif choice == '5':
            print("Exiting the Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
