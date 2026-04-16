"""Tạo một từ điển chứa:

thong_tin = {"ten": "Phi", "tuoi": 20, "diachi": "Đà Nẵng"}

In ra tất cả key, value và cặp key _ value."""
thong_tin = {"ten": "Phi", "tuoi": 20, "diachi": "Đà Nẵng"}
# In ra tất cả key:
print("Các key: ")
for x in thong_tin.keys():
    print(x)
# In ra tất cả value:
print("Các value: ")
for x in thong_tin.values():
    print(x)
# In ra các cặp key - value:
print("Các cặp key - value:")
for x, y in thong_tin.items():
    print(x,"-",y)
