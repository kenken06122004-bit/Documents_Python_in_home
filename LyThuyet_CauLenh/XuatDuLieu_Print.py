# Cú pháp câu lệnh print: print("obj", sep = seperator, end = end)
# Trong đó: + obj là các đối tượng trong python
#           + sep là phân cách giữa các đối tượng (nếu không có sep thì sẽ mặc định là dấu cách)
#           + end là chỉ ra kí tự được in ở cuối của dòng (nếu không có end thì mặc định là xuống dòng) 
# 1) Câu lệnh print():
print() # in ra một dòng không chứ dữ liệu
print(5)
print("Hello Word")
print(6) ; print("Hehe") # Dấu ; để phân biệt câu lệnh nào trước và sau giúp chúng ta có thể print nhiều dữ liệu trên 1 dòng code
print("Hello,","Nguyễn","Văn","Phi",sep=" ") # có sep nếu không có sep thì nó vẫn sữ tự động ngăn cách bằng khoảng trắng
print("Hello,","Nguyễn","Văn","Phi",sep=" ",end=".\n") # có end
# Lưu ý: khi muốn truyền số thì ta chỉ cần nhập số còn khi muốn truyền văn bản hay chuỗi thì ta phải có dấu ""
# Ngoài ra ta có một cái lưu ý: 
print("Tên = {0}","Họ = {1}".format("Phi","Nguyễn")) # Viết như này thì nó sẽ chỉ truyền số 2 vì hai cái 0 và 1 bị cách nhau
# bởi dấu ,
# Cách viết đúng là: chúng ta đưa dấu , vào dấu "" luôn
print("Tên = {0} , Họ = {1}".format("Phi","Nguyễn"))

