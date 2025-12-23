from configs.database import SessionLocal
from models.todo import Todo


def seed():
    db = SessionLocal()
    try:
        if db.query(Todo).count() == 0:
            db.add_all(
                [
                    Todo(title="Học FastAPI", priority=1),
                    Todo(title="Cài đặt Docker", priority=1, done=True),
                    # Thêm 3 cái nữa tại đây...
                ]
            )
            db.commit()
            print("Đã nạp dữ liệu mẫu thành công!")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
