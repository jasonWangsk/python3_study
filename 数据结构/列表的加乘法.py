"""
--append() 函数：末尾追加元素
+：把两组列表拼接成一个列表
* ：乘以一个数值n输出为列表的n倍数
"""
# +：把两组列表拼接成一个列表
l1 = ["你好","吗"]
l2 = ["?","哈哈哈哈"]
print(l1+l2)
x = l1+l2
x.append(1000000)
print(x)

# * ：乘以一个数值n输出为列表的n倍数
x = l1 * 3
print(x)

mylist = [1,2,3,22,11,34]
print(mylist*2)

for i in range(len(mylist)):  # 索引循环
    print(mylist[i])