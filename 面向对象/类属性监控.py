"""
类通过 __init__构造函数来初始化属于类的属性
：可以同过setter getter 进行属性的读写

传统属性监控 有几个属性必须绑定几个方法才能监控到

可以使用 魔法方法
:__getattr__ 方法获取类成员变量
:__setattr__ 方法来设置类成员变量
:__delattr__ 方法来删除类成员变量

"""


class Person:

    def __init__(self):
        self.age = 0

    def __setattr__(self, key, value):
        """魔法方法来设置类成员变量"""
        if key == "nianling":
            if value > 10:
                self.age = value
            else:
                print("年龄不合适")
        else:
            self.__dict__[key] = value  # 存储在类自己的字典中

    def __getattr__(self, item):
        if item == "nianling":
            return self.age

pp = Person()
pp.age = 20
print(pp.age)



class FangXing:

    def __init__(self):
        self.width = 0

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def del_width(self):
        self.width = 0

    mk = property(get_width,set_width,del_width)   # 通过属性绑定

fk = FangXing()
fk.mk = 100
print(fk.mk)
del fk.mk
print(fk.mk)

#
#
# fk.set_width(100)
# print(fk.get_width())


