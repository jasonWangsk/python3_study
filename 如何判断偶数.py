"""
1 随机生成1-100之间的数字
2 判断是否为整数，并计算整数个数和保存这些整数
3 输出结果

"""
import random
n = input("输入随机产生多少个整数：")
n = eval(n)
x = 0
count = 0  # 记录个数
result = ""  # 保存产生的偶数
while x < n:
    num = random.randint(1, 100)
    if num%2 == 0:
        count += 1
        result += str(num) + ","
    x += 1
print(f"共产生{str(count)}个偶数，分别是{result}")



"""
偶数：能被2整除的自然数，0除外
     除2余数为0的自然数

"""
print("\n","------------------------------------------")
num = 10
if num == 0:
    print(f"{num} 为自然数")
elif num % 2 == 0:
    print(f"{num} 为偶数")
    print(str(num) + "为偶数")
else:
    print(f"{num} 为奇数")
