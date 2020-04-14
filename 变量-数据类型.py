# 常量
age = 14
# 14不能被改变


# 变量 相当与数学中的未知数，存储在内存中
# 声明一个变量后就在内存中开辟一个空间来存储变量的值
"""
给变量赋值实际是传递新的常量的（内存）地址
"""
哈哈哈 = True
print(哈哈哈)
哈哈哈 = False
print(哈哈哈)
print(id(age))

#  关键字 keyword 不能用于变量命名

import keyword
print(keyword.kwlist)

# id
print(id(age))  # 变量内存地址
print(id(哈哈哈))  # 变量内存地址
"""python 变量是地址赋值"""

# float int str list  布尔 复数
num4 = "1223.345"
print(type(num4))
new_num4 = eval(num4) # 字符串转化成数值
print(type(new_num4))


bris = 19840909
money = 11003223.09
print(f'老王花了{money}元买了一件巴宝莉对风衣') # f - format 格式化输出
strs = "牛奶"
right = True
data_list = [1,3,5]
data = 4 + 6j # 复数--描述平面上对一个坐标
print(type(bris))
print(type(money))
print(type(strs))
print(type(right))
print(type(data_list))
print(type(data))

#  变量交互对称赋值
num1,num2,num3 = 1,2,3
print(num1,num2,num3)
miles = 100
kilometers = miles  * 2.609
print(kilometers)

# 多行合并一行 输出用分号分割
ab = 1; ac = 2; print(ab,ac)

# 变量数据交换
a = 6
b = 9
a,b = b,a
print(a,b)



