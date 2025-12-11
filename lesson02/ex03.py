# Bài tập 3: Hệ thống tag bài viết & người dùng
# Danh sách user: list tuple (user_id, name)
users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

# Dict bài viết: key là post_id, value là dict thông tin
posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}
# a. Tạo một dict user_map từ users, map user_id sang name
user_map = {}
for user_id, name in users:
    user_map[user_id] = name
print(user_map)

# b. Dùng vòng lặp duyệt posts.items() để in ra:
for post_id, post in posts.items():
  print(f'[{post_id}] {post["title"]} - {user_map[post["author_id"]]} - Tags: {", ".join(sorted(post["tags"]))}')

# c. Tạo một set all_tags chứa toàn bộ tag xuất hiện trong mọi bài viết
# for post_id, post in posts.items():
all_tags = set()
for post in posts.values():
    all_tags.update(post["tags"])
print(all_tags)

# d. Tạo một dict tag_counter để đếm số bài viết chứa mỗi tag
tag_counter = {}

for post in posts.values():
    for tag in post["tags"]:
        if tag not in tag_counter:
            tag_counter[tag] = 1
        else:
            tag_counter[tag] += 1

print(tag_counter)
