"""
 作用域：可以被影响的范围
   全局变量 声明在最外层 或 gloabl关键字
   局部变量 函数内部

"""

#  嵌套函数的调用 1
num = 15

def funa():
    num = 20
    # print(num)
    def funb():
        numb = 3
        print(num + numb)
    return funb
funa()()

#  嵌套函数的调用 2

def funa():
    num = 20
    # print(num)
    def funb():
        numb = 3
        print(num + numb)
    return funb()
funa()
