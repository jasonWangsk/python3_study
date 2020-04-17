"""
类的静态方法： 在类中的方法名称前加一个头 @staticmmethod
--加了装饰器后 不需要实例化就可以调用 类方
--不需要self 参数

类的类方法： 加一个头 @classmethod
--加了装饰器后 不需要实例化就可以调用 类方法
--需要 cls 参数
--是对类的构造方法分一个补充

静态方法用于一些自定义类实现一些通用功能

"""


# 类的静态方法//类的类方法

class Persion:
    age = ""  # 类属性

    def __init__(self):
        self.name = ""

    @staticmethod
    def say():
        print("我是静态方法，不需要类实例化就可以调用")

    @classmethod
    def set_age(cls, age):
        age = age
        print("类的类方法", age)


Persion.say()
Persion.set_age("18")
