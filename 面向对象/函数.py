"""
函数：就是完成特定功能到一个语句组/代码块
--形参和实参"
---定义函数时函数名后面括号中到变量名称叫做"形式参数"--- 参数名称
---在调用函数时函数名后面括号中到变量名称叫做"实际参数" ---参数值
def 关键字
函数return 有返回值
: 函数的参数就是函数内部的一个局部变量，参数只能影响函数内部，除非传入的是引用类型的参数

"""
# lambda 表达式 匿名函数  表示更简洁
function_la = lambda x,y:x*y
print(function_la(10,2))

function_la = lambda x,y:x%y
print(function_la(10,3))
print("*"*20)

# 普通函数定义
def func(x, y):
    return x * y
print(func(10,2))
print("*"*20)

# 函数的普通变量传参 global 全局变量的声明去影响函数外部的变量
x = 3
y = 4
def fun():
    global x,y
    x = 0
    y = -1
fun()
print(x,y)

# 递归函数
def age(n):
   if n == 1:
       return 10
   else:
       return age(n-1) + 2
print(age(5))

# 序列-字典传参 传入的是指针类型
print("*"*30)
dic = {"姓名":"老王","年龄":"30"}  # 定义一个字典
print(dic)
def funa(d):
    """修改字典值"""
    d["姓名"] = "lw"
    pass
funa(dic)
print(dic)

# 序列-列表传参 传入的是指针类型
print("*"*30)
lis = ["老王",30]  # 定义一个列表
print(dic)
def funa(d):
    """修改字典值"""
    d[1] = 18
    pass
funa(lis)
print(lis)
print("*"*30)

# 函数文档的定义方法：直接在自定义函数名下一行使用""" """来定义函数文档内容
# 使用函数__doc__，方法来查看
# 可以帮助在写api的时候自动生成函数说明
# 注释会被忽略，函数文档会被存储
print("查看函数文档内容：", funa.__doc__)

# 函数关键字参数与默认值 从最右边开始赋值
print("*"*30)
def func1(b,a=10):
    return a + b
print(func1(0))

# 可以给函数传参来改变关键字默认参数
print("*"*30)
def func2(name="lw",age="18"):
    return "姓名："+ name +" ,年龄："+age
print(func2())
print(func2("哈哈哈哈","26"))
print(func2("goood"))
print(func2(age="33"))

# 可变参数：只需要在函数参数前面加 *
print("*"*30)
def fu(*args):
    return args
print(fu("1",12121,[12131545])) # 输出的是元组类型 可以使用for 循环来逐个输出

# 可变参数 结合 普通关键字参数的用法
print("*"*30)
def add(*a,b):
    result = 0
    for i in a:
        result +=i
    result +=b
    return result
print(add(1,2,b=1))

def add(a,*b):
    result = a
    for i in b:
        result +=i
    return result
print(add(1,2,3))

# 可变参数 列表传参 拆解
print("*"*30)

lis = ["aaa",1,3232,-9]
def bb(*ll):
    for i in ll:
        print(i)
bb(lis)  # 不加* 直接输出列表
bb(*lis) # 加 * 直接输出列表元素

# print("*"*30)
# lis = ["aaa",1,3232,-9]
# def bb(ll):
#     for i in ll:
#         print(i)
# bb(lis)  # 不加* 直接输出列表
# bb(*lis) # 加 * 直接输出列表元素



# 可变参数 字典传参 拆解
print("*"*30)
dic = {"bs":"aaa","ll":000}
def bb(*ll):
    for i in ll:
        print(i)
bb(dic)  # 不加* 直接输出字典
bb(dic["bs"])
bb(*dic)# 加 * 直接输出字典的key

# **可变参数 调用的时候也要传入**
print("*"*30)
dic = {"bs":"aaa","ll":000}
def bb(**ll):
    print(ll)
bb(**dic)

print("*"*30)
dic = {"bs":"aaa","ll":000}
for j in dic.items():
    print(j)

print("hello".find("k"))
