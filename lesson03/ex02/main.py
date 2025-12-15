# Bài tập 2: Thống kê sản phẩm & hóa đơn
from exercises.lesson03.ex02.student_service import load_students_from_file, calc_avg_score, find_top_student, filter_failed

def main():
    while True:
        file_name = input("Nhập tên file điểm sinh viên:").strip()

        if file_name.lower() == 'exit':
            break

        try:
            student_list = load_students_from_file(file_name)
            if not student_list:
                print("Danh sách sinh viên trống")
                return
            avg = calc_avg_score(student_list)
            print(f"- Điểm trung bình lớp: {avg}")

            top_sv = find_top_student(student_list)
            if top_sv:
                print(f"- Sinh viên điểm cao nhất: {top_sv}")

            failed_list = filter_failed(student_list)
            print(f"- Danh sách sinh viên rớt ({len(failed_list)} sv):")
            if failed_list:
                for sv in failed_list:
                    print(f"   + {sv}")
            else:
                print("   (Không có)")

        except Exception as e:
            print(f"Lỗi: {e}")


if __name__ == "__main__":
    main()