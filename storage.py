import os
import json

FILENAME = "tasks.json"

def save_tasks(tasks: list) -> None:
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)

def load_tasks() -> list:
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        return json.load(file)