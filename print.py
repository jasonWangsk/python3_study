"""
print()函数输出默认换行
end="" 去除换行
sep="" 去除空格
"""

print(1, 123, 4, sep="")  # 去除空格
print(1, 123, 4, end="\n")  #

lis = [1,232,11,1,232,2,4,5]
newlis = set(lis)
print(newlis)


n = eval(input())
if n == 0:
    print("Hello World")
elif n > 0:
    print("He\nll\no \nWo\nrl\nd")
else:
    for c in "Hello World":
        print(c)