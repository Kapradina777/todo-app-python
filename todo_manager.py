from task import Task


class TodoManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        new_id = max((t.id for t in self.tasks), default=0) + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        return task

    def complete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            task.complete()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_pending(self) -> list[Task]:
        return [t for t in self.tasks if not t.done]

    def get_completed(self) -> list[Task]:
        return [t for t in self.tasks if t.done]

    def _find_task(self, task_id: int):
        return next((t for t in self.tasks if t.id == task_id), None)

    def load(self, data: list[dict]):
        self.tasks = [Task.from_dict(d) for d in data]

    def dump(self) -> list[dict]:
        return [t.to_dict() for t in self.tasks]