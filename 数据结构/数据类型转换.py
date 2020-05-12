"""
str
int
tuple
set
list
float
dict
"""
print(int("123"))
print(str(12))
print(float("123.123"))
print(tuple([1,2,3,4,5]))
print(set([1,2,3,4,5]))

# 进制转换
print(int("16",16))
print(int("16",10))
print(int("16",8))

print(hex(100))  # 16进制  6*16^1=96 +4*16^0 = 4 ==100
print(oct(10))  # 8 进制

# import os
# result = os.popen("df -h").read()
# # print(os.system("df -h"))
# print(result)

