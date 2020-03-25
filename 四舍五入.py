# round() 方法
# 四舍五入
num = 11.25
print(round(num))

num = 11.56
print(round(num))

# 保留小数点后 n 位数

num = 11.256823
print(round(num,3))
print(round(num,2))

# 拆分成元角分输出
money = 110.567
print(int(money),"元")
print(int(money * 10) % 10,"角")
print(int(round(money * 100) % 10),"分")



print(9%6)