"""
类的属性
 类似人类：姓名，身高，体重，职业，年龄等
 类等属性被开放出去可以直接调用赋值/取值

类的方法私有化:方法明前加 _ _
  类私有化方法的调用：可以采用类前加一个下划线和私有方法拼接调用
  如：（p._Person__say()
）

"""


class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __say(self):
        """类的方法私有化"""
        print("Hello:" + self.name)

    def  transfer_s(self):
        self.__say()


p = Person() # 实例化，p为实例化对象
p.set_name("哈哈哈")
print(p.get_name())
# 直接设置类等属性
p.name = "老王"
print(p.get_name())

# p.__say()  # 直接调用私有化方法会报错

#类私有化方法的外部调用
p._Person__say()

# 私有化方法内部调用
p.transfer_s()
print(p.__class__.__dict__)

print(hasattr(p,"name"))