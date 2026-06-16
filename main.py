from todo import create_task, complete_task, format_task, get_pending_tasks, get_completed_tasks
from storage import save_tasks, load_tasks


def show_menu():
    print("\n=== Todo App ===")
    print("1. Show all tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def show_all_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(format_task(task))


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append(create_task(new_id, title))
    print(f"✅ Task '{title}' added.")


def complete_task_cli(tasks):
    show_all_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to complete: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            complete_task(task)
            print(f"✅ Task '{task['title']}' completed.")
        else:
            print("Task not found.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_all_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            tasks.remove(task)
            print(f"🗑️ Task '{task['title']}' deleted.")
        else:
            print("Task not found.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            show_all_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task_cli(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()