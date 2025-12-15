def read_file_content(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def count_word_frequency(text: str) -> dict[str, int]:
    text = text.lower()

    punctuation = ".,;:?!()[]"
    for char in punctuation:
        text = text.replace(char, " ")

    words = text.split()

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

