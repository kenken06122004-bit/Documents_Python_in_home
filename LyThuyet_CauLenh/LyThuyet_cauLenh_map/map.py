with open("docFile.txt","r",encoding="utf_8") as f:
    n = int(f.readline().strip())
    ds_chieuCao = list(map(int,f.readline().split()))

lst = {} # dùng kiểu dữ liệu dictionary
for x in ds_chieuCao:
    if x in lst:
        lst[x] += 1
    else:
        lst[x] += 1