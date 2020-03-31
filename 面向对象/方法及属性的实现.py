"""
方法及属性的实现
"""

"""
# 1 属性的创建

"""
print("------------属性的创建------------")
class woman:
    pass
wangdama = woman()  # （类赋值给变量）实例化类

# 查看一个实例有哪些属性
print(wangdama.__dict__)
# 查看一个实例属于哪个类
print(wangdama.__class__)
# 查看一个实例所属类的属性
print(wangdama.__class__.__dict__)

# 给一个实例添加属性
wangdama.toufa = "黄色"
# 查看实例的属性
print(wangdama.__dict__)  # 输出为字典 {'toufa': '黄色'}

liudama = woman()  # 其他实例添加属性相互独立不受影响
liudama.xiezi = "黑色"  # 给实例添加属性
print(liudama.__dict__)  # 查看实例属性


# 如果修改类属性的时候，该类下所有实例类的其他实例的类属性都会受影响

liudama.__class__.yifu = "蓝色"
print(liudama.__class__.__dict__)
print(wangdama.__class__.__dict__)

print("-----------方法的创建-------------")

"""
# 2 方法的创建

"""
# 方法和函数的区别就是函数没有 self 参数
# 类是抽象的不能直接调用方法 必须使用具体的对象 实例去调用
class god:
    def a(self):   # self 是必须的 所有的方法第一个参数必须是self，代表所有实例共享这个方法，self不具备任何含义
        print("哈哈哈来唱歌")

# god.a()  # 不可以直接通过类调用方法
god().a() # god类 的实例调用


doit = god() # 实例化类 1
doit.a()  # 调用方法
# 对于类所有的实例都可以调用这个方法
runit = god() # 实例化类 2
runit.a()

print("------------隐藏属性和隐藏方法------------")
"""
3 隐藏属性和隐藏方法 （__双下划线）
"""
class school:
    def __banji(self):
        print("学生班级")
# school().__banji()  # 不能调用

print("------------类专有方法------------")
"""
4 类专有方法
"""
#  __init__ 构造函数 不要调用直接执行
# 函数开始时直接初始化构造起来
class people:
    def hi(self):
        print(8899)
    def __init__(self):
        a = "how are you!!"
        b = "me too!!"
        print(a+b)
people()

#  __del__ 析构函数
# 对象执行到最后到时候释放对象
# 系统自带 不需要单独写
class friend:
    def hi(self):
        print(8899)
    def __init__(self):
        print("init最先调用")
    def __del__(self):
        a = "del析构函数"
        b = "--对象生命周期结束，释放/删除对象！"
        print(a+b)
xiaohuang = friend()  # 生成实例赋值给 xianghuang 对象
