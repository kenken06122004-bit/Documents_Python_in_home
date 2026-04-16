def chuyenSo(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
# In bang cuu chuong:
for i in range(2,10): # 10 - 1 = 9
    print("Bang cuu chuong",i)
    for j in range(1,11): # 11 - 1 = 10
        print(i,"x",j,"= {}".format(i*j))