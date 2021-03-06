"""
for 语句嵌套 while
for for嵌套
while for嵌套
while while嵌套

一维列表：
list1 = ["a","b"]
list2 = ["c","d"]

二维列表：
list3 = [list1, list2]

多维列表:
list4 = [list3]

"""

# 遍历列表中嵌套字典 输出不同的字典
list_a = [{"name":"jason","age":18,"ps":9},
        {"name": "kkaa", "age": 30, "ps": 0}]

list_new = [{"name":"jason","age":18,"ps":9},
        {"name": "kkaa", "age": 30, "ps": 0},
         {"name": "cc", "age": 20, "ps": 0}]

data_source = None

for one in list_new:
    if one not in list_a:
        data_source = one
        print(data_source)
# 结合接口测试返回进行断言。。。
assert data_source != None
assert data_source['name'] == "cc"
# -------------------------------------


list1 = ["a","b"]
list2 = ["c","d"]
list3 = [list1, list2]  # 二维数组
list4 = [list3]  # 多维列表

print("输出二维数组")
for i in list3:
    print(i)

print("输出多维列表")
for j in list4:
    print(j)
    for k in j:
        print(k)

print("-------------------")

x = "abc"
print(len(x))
x = [1,"a",23,"ll"]
print(len(x))
print("*****************")
for i in range(0,len(x)):
    print(i)
print("*****************")

num1 = 30
if num1 % 2 == 00:
    print(num1 % 2)
print(2)

num1 = 35
if num1 % 2 == 00:
    print(1)
else:
    print(num1 % 2)


x = 2
y = 3
if x > 2:
    if y > 2:
        z = x + y
        print("z is", z)
    else:
        print("x is",x)

x = 3
y = 2
if x > 2:
    if y > 2:
        z = x + y
        print("z is", z)
    else:
        print("x is",x)

x = 3
y = 3
if x > 2:
    if y > 2:
        z = x + y
        print("z is", z)
    else:
        print("x is",x)