"""
自定义序列的实现
序列：字典/元组/列表

继承内建类
 :使用 内建类的目的提过写代码效率
 可以提升更多功能
"""


class Mdic:

    def __init__(self):
        """自定义序列的实现"""
        self.length = 0
        self.dica = {}

    def __len__(self):
        """通过序列操作 获取字典的长度"""
        return self.length

    def __setitem__(self, key, value):
        """模拟序列设置字典"""
        self.dica[key] = value
        self.length += 1
        print("字典增加了一项：", key, value)

    def __getitem__(self, item):
        """模拟序列获取字典"""
        return self.dica[item]

    def __delitem__(self, key):
        """模拟删除字典"""
        del self.dica[key]
        self.length -= 1
        print("字典删除了一项：", key)

#
# md = Mdic()
# md["aaa"] = "lw"
# print("字典长度：", len(md), md.dica)
# md["bbb"] = "454545"
# print("字典长度：", len(md), md.dica)
# md["ccc"] = "哈哈哈哈哈"
# print("字典长度：", len(md), md.dica)
#
# del md["ccc"]
# print("字典长度：", len(md), md.dica)
#
# print("获取字典", md["bbb"])
#
print("*"*20)
"""
继承 内建类使用
"""

class NjList(list):

    def __init__(self, *args):
        super(NjList, self).__init__(*args)

    def __getitem__(self, item):
        return super().__getitem__(item)


lis1 = NjList(("哈哈哈","忸怩你"))
print(lis1)
del lis1[0]
print(lis1)

"""
内建类 自定义 字典
"""

class Mdict(dict):

    def __init__(self, *args):
        return super().__init__(*args)


mdd = Mdict({"a":12})
print(mdd)











