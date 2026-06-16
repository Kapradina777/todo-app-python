from todo_manager import TodoManager
from storage import save_tasks, load_tasks


def show_menu():
    print("\n=== Todo App ===")
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def show_all_tasks(manager):
    if not manager.tasks:
        print("No tasks yet.")
        return
    for task in manager.tasks:
        print(task)


def main():
    manager = TodoManager()
    manager.load(load_tasks())

    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            show_all_tasks(manager)

        elif choice == "2":
            title = input("Task title: ").strip()
            if title:
                task = manager.add_task(title)
                print(f"✅ Added: {task}")
            else:
                print("Title cannot be empty.")

        elif choice == "3":
            show_all_tasks(manager)
            try:
                task_id = int(input("Enter task ID to complete: "))
                if manager.complete_task(task_id):
                    print("✅ Task completed.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            show_all_tasks(manager)
            try:
                task_id = int(input("Enter task ID to delete: "))
                if manager.delete_task(task_id):
                    print("🗑️ Task deleted.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            save_tasks(manager.dump())
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()