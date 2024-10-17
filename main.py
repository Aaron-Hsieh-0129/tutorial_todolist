# main.py
from todo import TaskManager

def show_menu():
    """Display the menu options to the user."""
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit")

if __name__ == '__main__':
    task_manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            task_manager.add_task(task_name)
        elif choice == '2':
            task_manager.show_tasks()
            task_index = int(input("Enter the number of the task to delete: ")) - 1
            task_manager.delete_task(task_index)
        elif choice == '3':
            task_manager.show_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

