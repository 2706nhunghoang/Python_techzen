# Bài tập 3: To-do List theo ngày với DateTime + File + OOP + Exception
from datetime import datetime
from models import Task
import task_service

FILENAME = "tasks.txt"

def print_tasks(tasks: list[Task]) -> None:
    print("\n--- DANH SÁCH TẤT CẢ ---")
    if not tasks:
        print("Danh sách trống.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def print_overdue_tasks(tasks: list[Task]) -> None:
    print("\n--- DANH SÁCH QUÁ HẠN ---")
    now = datetime.now()
    overdue_tasks = [t for t in tasks if t.is_overdue(now)]

    if not overdue_tasks:
        print("Không có công việc nào quá hạn.")
    else:
        for task in overdue_tasks:
            print(f"- {task}")
def add_new_task(tasks: list[Task]) -> None:
    print("\n--- THÊM TASK MỚI ---")
    print("(Gõ 'exit' để quay lại menu)")
    while True:
        desc = input("Nhập mô tả công việc: ").strip()
        if desc.lower() == 'exit': return

        date_input = input("Nhập ngày hết hạn (YYYY-MM-DD): ").strip()
        if date_input.lower() == 'exit': return

        try:
            due_date = datetime.strptime(date_input, "%Y-%m-%d")
            new_task = Task(desc, due_date)
            tasks.append(new_task)

            task_service.save_tasks(FILENAME, tasks)
            print("Thêm thành công!")
            break
        except ValueError:
            print("Lỗi: Định dạng ngày sai! (Ví dụ: 2025-01-30) Hãy nhập lại")

def mark_task_done(tasks: list[Task]) -> None:
    print("\n--- ĐÁNH DẤU HOÀN THÀNH ---")
    print_tasks(tasks)

    try:
        idx = int(input("Nhập số thứ tự task muốn đánh dấu Done: "))
        if 1 <= idx <= len(tasks):
            selected_task = tasks[idx - 1]
            if selected_task.status == "done":
                print("Task này đã xong từ trước rồi!")
            else:
                selected_task.status = "done"
                print(f" Đã đánh dấu xong: {selected_task.description}")
                task_service.save_tasks(FILENAME, tasks)
        else:
            print("Số thứ tự không tồn tại.")
    except ValueError:
        print("Vui lòng nhập con số nguyên.")

def main():
    tasks = task_service.load_tasks(FILENAME)

    while True:
        print("\n--- QUẢN LÝ CÔNG VIỆC ---")
        print("1. Xem tất cả task")
        print("2. Xem các task quá hạn")
        print("3. Thêm task mới")
        print("4. Đánh dấu task là done")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ").strip()
        match choice:
            case '1':
                print_tasks(tasks)

            case '2':
                print_overdue_tasks(tasks)

            case '3':
                add_new_task(tasks)

            case '4':
                mark_task_done(tasks)

            case '5':
                print("Tạm biệt!")
                break

            case _:
                print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()