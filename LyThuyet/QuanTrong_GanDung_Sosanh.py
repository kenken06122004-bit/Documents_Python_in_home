# Nếu sau này phải so sánh gần đúng để làm việc với số thực (float) thì ta phải tính sai số như 1e-3 hay 1e-6. Quá phức tạp nên
# ta sẽ dùng hàm có sẵn trong math
# đó chính là: math.isclose
#         elif ((math.isclose(a, b) and math.isclose(a**2 + b**2, c**2)) or
#         (math.isclose(a, c) and math.isclose(a**2 + c**2, b**2)) or
#         (math.isclose(b, c) and math.isclose(b**2 + c**2, a**2))):
#          print("Đây là tam giác vuông cân")