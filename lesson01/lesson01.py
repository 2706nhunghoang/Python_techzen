# BTTH7: Viết lại các bài tập đã làm bằng hàm

# 7a. Hàm tính tổng từ 1 đến n
# sum_to_n(n: int) -> int
def sum_to_n(n: int) -> int:
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(f"==> Tổng từ 1 đến {3} là: {sum_to_n(3)}")

# 7b. Hàm kiểm tra năm nhuận
#
# is_leap_year(year: int) -> bool
def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(f"==> Năm 2025 {" là năm nhận" if is_leap_year(2025) else "không phải là năm nhuận"}")


# 7c. Hàm đếm ký tự
# count_char(string: str, char: str) -> int
def count_char(string: str, char: str) -> int:
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count
print(f"==> Tổng số kí tự A trong A1A2A3: {count_char("A1A2A3", "A")}")
# BTTH8: Viết hàm định dạng tên với optional middle name
def format_name(first: str, last: str, middle: str | None = None) -> str:
    if middle:
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"
print("==> Định dạng tên")
name1 = format_name("John", "Doe")
print(f"TH1: {name1}")  # Output: John Doe
name2 = format_name("John", "Doe", "William")
print(f"TH2: {name2}")  # Output: John William Doe
name3 = format_name(first="Lan", middle="Thị", last="Nguyễn")
print(f"TH3: {name3}")  # Output: Lan Thị Nguyễn

# BTTH9: Chuẩn hóa họ tên
def normalize_name(name: str) -> str:
    result = []
    if not name: return result
    for word in name.split():
        new_word = word[0].upper() + word[1:].lower()
        result.append(new_word)

    return " ".join(result)
# Test
raw_name = "  nGuyEn vAn a   "
print(f"==> Chuẩn hóa tên '  nGuyEn vAn a   ' => {normalize_name(raw_name)}")

# BTTH10: Kiểm tra chuỗi đối xứng
def is_palindrome_loop(text: str) -> bool:
    length = len(text)

    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            return False

    return True

print(f"==> Kiểm tra đối xứng chuỗi 'madam' => {is_palindrome_loop("madam")}")
print(f"==> Kiểm tra đối xứng chuỗi 'level' => {is_palindrome_loop("level")}")
print(f"==> Kiểm tra đối xứng chuỗi '122 1' => {is_palindrome_loop("122 1")}")

# BTTH11: Đếm số lượng nguyên âm trong chuỗi
def count_vowels(text: str) -> int:
    vowels = "ueoaiUEOAI"
    count = 0
    for char in text:
        if char in vowels:
            count += 1

    return count
print(f"==> Số lượng nguyên âm trong chuỗi 'AaBSe' là {count_vowels("AaBSe")}")