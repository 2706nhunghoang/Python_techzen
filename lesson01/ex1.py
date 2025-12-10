# Bài tập 1: Kiểm tra và tìm ngày kế tiếp, ngày trước đó
    # Nhập vào thông tin 1 ngày (ngày – tháng – năm)
    # Kiểm tra ngày có hợp lệ hay không?
    # Nếu hợp lệ hãy tìm ra ngày kế tiếp (ngày – tháng – năm) & ngày trước đó (ngày – tháng – năm)

# Bước 1
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

# Bước 2
leap = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

days_in_month = [0, 31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Bước 3
if not (y > 0 and 1 <= m <= 12 and 1 <= d <= days_in_month[m]):
    print(f"Ngày {d}/{m}/{y} KHÔNG hợp lệ.")
else:
    print(f"Ngày {d}/{m}/{y} hợp lệ.")

    # Tìm ngày kế tiếp
    nd, nm, ny = d + 1, m, y
    if nd > days_in_month[m]:
        nd = 1
        nm += 1
        if nm > 12:
            nm = 1
            ny += 1
    print(f"Ngày kế tiếp: {nd}/{nm}/{ny}")

    # tìm ngày trước đó
    pd, pm, py = d - 1, m, y
    if pd < 1:
        pm -= 1
        if pm < 1:
            pm = 12
            py -= 1
        pd = days_in_month[pm] if pm != 12 else 31

    print(f"Ngày trước đó: {pd}/{pm}/{py}")
