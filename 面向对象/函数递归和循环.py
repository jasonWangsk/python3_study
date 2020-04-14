"""
在定义的函数内部 调用函数自己形成一个回路
，必须要有一个退出的方式（一般采用条件判断来实现）

：1 函数要自我调用 2 要有退出条件 3 要少用递归因为消耗内存
"""

for i in range(1,11):
    print(i, end=",")
print()
print("*"*20)

# 递归例子
# 利用函数输出1--10的数字
n = 1
def digui(a):
    print(a)
    if a >= 10:
        return a
    a+= 1
    digui(a)
digui(n)

print("*"*20)

# 阶乘的计算
"""
阶乘理解：
0！= 1
1！= 1*1
2！= 2 * 1
3！= 3 * 2 * 1
4！= 4*3*2*1
。。。。。
"""
# 采用函数递归的方式进行计算
x = 0
def jiecheng(y):
    if y >=10:
        return y
    y +=1
    z = y *  (x+1)
    print(z)
    jiecheng(y)
jiecheng(x)