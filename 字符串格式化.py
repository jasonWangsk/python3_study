print(10, 100, 2000, 3000, 20)
print(10, 1000, 20000, 3000, 200)
print(10, 10000, 200000, 30000, 2000)

# 5代表宽度 <代表左对齐（默认右对齐） d代表整数 f代表实数 s代表字符串
print(format(10,"<5d"), 100, 2000, 3000, 20)
print(format(100,"<5d"), 1000, 20000, 3000, 200)
print(format(1000,"<5d"), 10000, 200000, 30000, 2000)

a = 1
b = 9
if a is b:
    print(True)
elif a is not b:
    print(False)
