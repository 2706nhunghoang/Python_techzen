# Bài tập 2: Quản lý điểm sinh viên với File I/O + OOP + Exception
from utils import file_utils
def main():
    while True:
        file_name = input("Nhập tên file cần phân tích:").strip()

        if file_name.lower() == 'exit':
            break

        try:
            content = file_utils.read_file_content(file_name)

            word_counts = file_utils.count_word_frequency(content)

            total_words = sum(word_counts.values())
            print(f"\nTổng số từ: {total_words}")

            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

            print("Top 10 từ xuất hiện nhiều nhất:")
            for word, count in sorted_words[:10]:
                print(f"- {word}: {count}")

        except FileNotFoundError:
            print(f" Lỗi: File '{file_name}' không tồn tại.")
        except Exception as e:
            print(f" Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()