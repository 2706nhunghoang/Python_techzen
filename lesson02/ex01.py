# Bài tập 1: Quản lý học viên & khóa học

# Danh sách học viên (list các tuple)
students = [
    ("SV01", "Nguyen Van A", 20),
    ("SV02", "Tran Thi B", 21),
    ("SV03", "Le Van C", 19),
]

# Dict lưu điểm từng môn cho từng sinh viên
scores = {
    "SV01": {"math": 8.0, "python": 7.5},
    "SV02": {"math": 6.5, "python": 8.5},
    "SV03": {"math": 9.0, "python": 9.5},
}

# Set các môn học hiện có
courses = {"math", "python"}

# a. Dùng vòng lặp + unpacking tuple để in ra danh sách học viên theo format
for student in students:
  student_id, name, age = student
  print(f"{student_id} - {name} ({age})")

# b. Tạo một list mới python_scores chỉ chứa tuple (student_id, name, python_score)
python_scores = [(student_id, name, scores[student_id]["python"]) for student_id, name, _ in students]
print(python_scores)

#  c. Tìm học viên có điểm Python cao nhất từ python_scores và in ra: Top Python: <name> - <score>
top_python_score = python_scores[0]
for score in python_scores:
  if score[2] > top_python_score[2]:
    top_python_score = score

print(f'Top Python: {top_python_score[1]} - {top_python_score[2]}')

# d. Thêm môn mới "database" vào courses (dùng set) và gán tạm điểm database = 0 cho tất cả sinh viên trong scores
courses.add("database")
print(f'New courses: {courses}')

for id, _, _ in students:
  scores[id]["database"] = 0
print(f'New scores: {scores}')