# Bài tập 2: Thống kê sản phẩm & hóa đơn

# Mỗi sản phẩm là 1 tuple (product_id, name, price)
products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]

# Danh sách đơn hàng (list dict)
orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]
# a. Tạo một dict product_map từ products để tra cứu nhanh theo product_id với dạng:
product_map = {}
for product in products:
    product_map[product[0]] = {"name":product[1], "price":product[2]}
print(product_map)

# b. Với mỗi hóa đơn trong orders, hãy tính tổng tiền của hóa đơn đó, lưu vào key mới "total" trong từng dict hóa đơn
for order in orders:
  total = 0
  for id in order["items"]:
    total += product_map[id]["price"]
  order["total"] = total
print('\n', orders)

# c. In ra danh sách hóa đơn theo format
#     HD01: 3 san pham, Tong tien = ...
for order in orders:
    print(f"{order['order_id']}: {len(order['items'])} sản phẩm, Tổng tiền = : {order['total']}")

# d. Tạo một set all_products_sold chứa tất cả product_id đã từng được bán trong mọi hóa đơn, sau đó in ra:
all_products_sold = set()
for order in orders:
    for item in order["items"]:
        all_products_sold.add(item)

print(f"So luong san pham khac nhau da ban: {len(all_products_sold)}")
