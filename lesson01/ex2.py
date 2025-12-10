# Bài tập 2: Tính tổng S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!
# > **Đề bài:**
# > Viết chương trình tính `S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!`, với n được nhập từ bàn phím
#
# ---# Bài tập 2: Tính tổng S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!
#
# > **Đề bài:**
# > Viết chương trình tính `S = 1 + 1/3! + 1/5! + ... + 1/(2n−1)!`, với n được nhập từ bàn phím
#
# ---
def calculate_S_manual(n: int) -> float:
    s = 0
    for i in range(1, n*2, 2):
        print("i", i)
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        s += 1 / fact

    return s
print(f"Tổng S = {calculate_S_manual(2)}")