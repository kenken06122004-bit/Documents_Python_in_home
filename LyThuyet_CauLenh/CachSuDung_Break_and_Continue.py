# break dùng để thoát ra vòng lặp gần nhất chứa nó
for i in range(0,10):
    print(i)
    if i > 5:
        break
# continue bỏ qua các câu lệnh dưới nó nếu điều kiện đúng và quay lại vòng lặp 
for i in range(0,10):
    if i % 2 == 1:
        continue
    print(i)