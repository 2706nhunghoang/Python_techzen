from datetime import datetime

class Task:
    def __init__(self, description: str, due_date: datetime, status: str = "todo"):
        self.description = description
        self.due_date = due_date
        self.status = status

    def is_overdue(self, now: datetime) -> bool:
        if self.status == "done":
            return False
        return self.due_date < now

    def __str__(self) -> str:
        date_str = self.due_date.strftime("%Y-%m-%d")
        status_icon = "[DONE]" if self.status == "done" else "[TODO]"

        return f"{status_icon} {self.description} (Hạn: {date_str})"