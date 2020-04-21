"""
可以看作集合，集合类似列表，但迭代器消耗内存资源小于集合

迭代：循环

在python中表现为 __iter__ 内建方法，必须要返回一个迭代器
  一个类只要有__iter__ 方法，那么这个类就是一个迭代器
  每一次迭代返回结果在 __next__ 方法中

for 循环来输出结果

--------------
生成器
  生成器和迭代器都是一个值一个值生成的
  区别：
  迭代器依靠类，生成器依靠自定义函数
  迭代器使用__iter__和__next__方法
  生成器使用 yield 关键词 实现生产值
  利用循环思想lai
yield: 使得函数暂停，并且提交一个生成的值

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


# 生成器--随机生成列表中的元素
import random

def num_list():
    num_list = []
    for i in range(10):
        num_list.append(random.randint(1,10))
    print(num_list)
    # 制作生成器
    for j in num_list:
        yield j

for l in num_list():
    print(l,end="-->")

# 生成器使用 next() 函数来迭代返回值
#  next() 返回迭代器的下一项。如果指定了默认值并且迭代器已用尽，则返回它而不是提高StopIteration。
def num_iter():
    num_iter = [1, 7, 5, 7, 7, 10, 5, 1, 7, 1]
    for i in num_iter:
        yield i

# 使用 变量来表示一个实际生成器对象
xx = num_iter()
print('\n',num_iter())
print(next(xx))
print(next(xx))
print(next(xx))