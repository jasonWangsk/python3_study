"""
while 条件判断：
满足判断条件的情况下，多条执行语句，条件判断的结果为True or False

for 循环
for 值 in 数组范围

嵌套循环
range()函数
"""

print("**********************")
for i in range(2,9):
    if i ==5:
        continue
    print(i)


print("**********************")
for i in range(2,9):
    if i ==5:
        break
    print(i)

#输出1-100
for i in range(1,101):
    print(i)

print("**********************")
lit = ["哈哈","help",12,"jason"]
n = 1
for i in lit:
    if n ==len(lit):
        print(i)
    else:
        print(i,end=",")
    n += 1
print("**********************")


x = 0
# while x<100:
#     x += 1
#     print(x)


while x < 7:
    x +=1
    if x ==5:
        continue;  # =5 跳过继续下面的循环，，如果break 直接退出循环不进行下面的循环语句

    print(x)


#
#
# name = input("name:")
# while name == "old":
#     print("good")
#     break   # 得到结果后退出