"""

"""

# 表达式eval("500/10)的结果
print(eval("500/10"))
print(type(eval("45")))

#表达式 divmod(20,3) 结果：
# divmod() 函数返回一个元组 如20/3 的商和余数 的元组
print(divmod(20,3))

x = "aa"
print(x*3)
print(len(x))
x.upper()
y = x.replace("aa","6666")
print(y)

# 把字符串第一个字母大写 其他字母小写
str = 'python'
print(str[0].upper() + str[1:])

# 执行以下程序输出结果
w = "93python22"
for x in w:
    if "0"<=x<="9":
        continue
    else:
        w.replace(x,'')
print(w)

# 执行以下程序输出结果
la = "python"
# try:
#     s = eval(input("请输入整数："))
#     ls = s*2
#     print(ls)
# except:
#     print("请输入整数：")

# 执行以下程序输出结果
s = 0
def fun(num):
    try:
        s += num
        return s
    except:
        return 0
    return 5
print(fun(2))

# 执行以下程序输出结果
ss = list(set("jzzszyj"))
ss.sort()
print(ss)

# 执行以下程序输出结果
ss = set("htslbht")
sorted(ss)
for i in ss:
    print(i)

# 执行以下程序输出结果
ls1 = [1,2,3,4,5]
ls2=ls1
ls3 = ls1.copy()
print(id(ls2),id(ls3))

# 执行以下程序输出结果
import random
ls1 = [12,34,56,78]
random.shuffle(ls1)
print(ls1)

# 执行以下程序输出结果
# fo = open("text.csv",'w')
# x = [90,87,93]
# z = []
# for y in x:
#     z.append(str(y))
# fo.write(",".join(z))
# fo.close()

# M = 10
# N = 100
# op = input()
#
# if op == "1":
#     print('%.2f' % (M+N))
# elif op == "2":
#     print('%.2f' %(M/N))


# s = input()
# print("{:.2f}".format(eval(s)))
#
# n = eval(input())
# if n == 0:
#     print("Hello World")
# elif n > 0:
#     print("He\nll\no \nWo\nrl\nd")
# else:
#     for c in "Hello World":
#         print(c)


print(pow(-1,0.5))

a = 10
print("+"*30+"%.3f" % pow(a,0.5))

s = "Alice-Bob-Charis-David-Eric-Flurry"
print(s[0:4] +"+" + s[-6:])

# k = 10000
# while k>1:
#     print(k)
#     k /=2

for s in "PYTHON":
   if s=="T":
      continue
   print(s,end="")

str1 = "Runoob example....wow!!!"

str2 = "example"
print(str1.find(str2,5))


def f(a,b):
  a=4
  return  a+b
def main():
  a=5
  b=6
  print(f(a,b),a+b)
main()

print(4**2)

print("{}".format(random.randint(5, 10)))

count = 0
while count<5:
    print("{}".format(random.randint(5, 10)))
    count -=1

