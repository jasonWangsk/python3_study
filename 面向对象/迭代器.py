"""
可以看作集合，集合类似列表，但迭代器消耗内存资源小于集合

迭代：循环

在python中表现为 __iter__ 内建方法，必须要返回一个迭代器
  一个类只要有__iter__ 方法，那么这个类就是一个迭代器
  每一次迭代返回结果在 __next__ 方法中

for 循环来输出结果

"""

# 利用迭代器 输出一个三角形

class Triangle:

    def __init__(self):
        self.s = 1

    def __iter__(self):
        return self

    def __next__(self):
        strr = "*" * (2*self.s-1)
        self.s +=1
        if len(strr) > 15:
            raise StopIteration    # 使用raise 主动抛出异常停止迭代
        return strr


md = Triangle()

for j in md:
    print(j)


for i in  md:
    if len(i) > 19:
        break
    print(i)