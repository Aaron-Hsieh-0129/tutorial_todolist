# todo.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        """Add a new task to the to-do list."""
        self.tasks.append(task_name)

    def delete_task(self, task_index):
        """Delete a task from the to-do list based on its index."""
        # TODO2: Implement the delete_task method
        pass

    def show_tasks(self):
        """Display the list of tasks."""
        if not self.tasks:
            print("No tasks added yet.")
            return

        print("\nCurrent To-Do List:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

