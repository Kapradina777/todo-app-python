class Task:
    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self.done = False

    def complete(self):
        self.done = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(data["id"], data["title"])
        task.done = data["done"]
        return task

    def __str__(self) -> str:
        status = "✅" if self.done else "⬜"
        return f"{status} [{self.id}] {self.title}"