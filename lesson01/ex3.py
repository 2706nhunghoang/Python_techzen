# Bài tập 3: Thao tác chuỗi
# > **Đề bài:**
# > Viết chương trình để chuẩn hoá câu:
# >* Bỏ khoảng trắng thừa (giữa các từ chỉ còn 1 khoảng trắng)
# >* Viết hoa chữ cái đầu câu
# >* Đảm bảo câu kết thúc bằng chính xác một dấu chấm “.”
# >  * Nếu thừa nhiều dấu chấm liên tiếp thì rút gọn còn “.”
# >
# > Ví dụ: "Hello worlD, this Is python.. " => "Hello world, this is python."

def normalize_sentence(text: str) -> str:
    text = text.lower().strip()

    words = text.split()
    text = " ".join(words)
    text = text.rstrip('. ')
    text += '.'

    if len(text) > 0:
        text = text[0].upper() + text[1:]

    return text

input_str = "Hello worlD, this Is python.. "
print(f"Output: '{normalize_sentence(input_str)}'")
