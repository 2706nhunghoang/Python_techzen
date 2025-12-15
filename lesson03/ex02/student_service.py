from exercises.lesson03.ex02.models import Student
import csv

def load_students_from_file(filename: str) -> list[Student]:
    students = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=2):
                try:
                    name = row['Tên'].strip()
                    age = int(row['Tuổi'].strip())
                    score = float(row['Điểm'].strip())
                    student = Student(name, age, score)
                    students.append(student)
                except ValueError as e:
                    print(f"Cảnh báo dòng '{i}': Dữ liệu sai format -> {e}")
        return students
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file: {filename}")

def calc_avg_score(students: list[Student]) -> float:
    if not students:
        return 0.0
    total_score = sum(sv.score for sv in students)
    return round(total_score / len(students), 2)


def find_top_student(students: list[Student]) -> Student | None:
    if not students:
        return None
    return max(students, key=lambda sv: sv.score)


def filter_failed(students: list[Student]) -> list[Student]:
    return [sv for sv in students if not sv.is_passed()]