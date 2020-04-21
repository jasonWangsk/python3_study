"""
异常 分类
    1、自动抛出异常，编译器自动判断抛出异常
    2、手动抛出异常：使用 raise Exception

try
...
except
语句中扑获异常，如果异常类名太长可以用 as 取别名

---
异常类型结构,必须要有try，
try:
except:
else:
finally:

"""
age = 16

if age > 18:
    raise Exception("....")

try:
    if age <= 18:
        print(age)

finally:
    print("哈哈哈哈")

# 自定义异常类
class MyException(Exception,BaseException):

    def __init__(self,code=202,desc="异常消息:"):
        self.code = code
        self.desc = desc
        # self.msg = msg


a = input("输入一个数值：")

try:
    if not a.isdigit():
        raise MyException
except MyException as me:
    print(me.desc,me.code)


# 类的异常利用
# 使用 hasattr()函数 来判断类属性是否存在
print("*"*20)
class MClass:

    def abc(self):
        print("类属性。。。。")

mc = MClass()
if hasattr(mc,"ac"):
   mc.abc()  # 未输出该方法
   mc.abd()
else:
    print("属性不存在")
print("*"*20)

try:
    mc.abc()  # 不管是否失败都执行
    mc.abd()
except:
    print("属性不存在")

