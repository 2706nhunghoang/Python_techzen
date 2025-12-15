from datetime import datetime
from models import Task

DATE_FORMAT = "%Y-%m-%d"

def load_tasks(filename: str) -> list[Task]:
    tasks = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line: continue

                try:
                    parts = line.split(';')
                    if len(parts) != 3:
                        raise ValueError("Sai số lượng cột")

                    desc = parts[0]
                    date_str = parts[1]
                    status = parts[2]

                    due_date = datetime.strptime(date_str, DATE_FORMAT)

                    task = Task(desc, due_date, status)
                    tasks.append(task)

                except ValueError as e:
                    print(f"Cảnh báo dòng {line_num}: Dữ liệu lỗi ({e}) -> Bỏ qua.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {filename}")
    return tasks


def save_tasks(filename: str, tasks: list[Task]) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for task in tasks:
                date_str = task.due_date.strftime(DATE_FORMAT)
                line = f"{task.description};{date_str};{task.status}\n"
                f.write(line)
        print("Đã lưu dữ liệu thành công!")
    except IOError as e:
        print(f"Lỗi khi ghi file: {e}")