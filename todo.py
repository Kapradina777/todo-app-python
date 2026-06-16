def create_task(task_id: int, title: str) -> dict:
    return {
        "id": task_id,
        "title": title,
        "done": False
}

def complete_task(task: dict) -> dict:
    task["done"] = True
    return task

def format_task(task: dict) -> str:
    status = "✅" if task["done"] else "⬜"
    return f"{status} {task['title']} (ID: {task['id']})"

def get_pending_tasks(tasks: list) -> list:
    return [task for task in tasks if not task["done"]]

def get_completed_tasks(tasks: list) -> list:
    return [task for task in tasks if task["done"]]

