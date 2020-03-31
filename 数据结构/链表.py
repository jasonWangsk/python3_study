"""
链表：是一种非连续，非顺序到存储方式
 -- 由一系列结点点组成，每个结点包括数据域 和 指向另一个结点到指针域
 -- 可以分为单向//双向链表，单向//双向循环链表

"""

# 单向链表实现

class JieDian:

    def __init__(self, data):
        """结点类"""
        self.data = data  # 数据域
        self.next = None  # 指针域默认为空


class LinkList:

    def __init__(self, jiedian):
        """链表类"""
        self.head = jiedian  # 链表到表头
        self.head.next = None  # 下一个结点位置
        self.tail = self.head  # 表头和表尾初始是重合的

    def add(self, jiedian):
        self.tail.next = jiedian
        self.tail = self.tail.next  # 表尾移动

    def view(self):
        jiedian2 = self.head
        linkstr = ""
        while jiedian2 is not None:
            if jiedian2.next is not None:
                linkstr = linkstr + str(jiedian2.data) + "-->"
            else:
                linkstr += str(jiedian2.data)
            jiedian2 = jiedian2 .next
        print(linkstr)
# 声明结点
jd1 = JieDian(7)
jd2 = JieDian("hello")
jd3 = JieDian(8899)
jd4 = JieDian(0)

# 链表链接
x = LinkList(jd1)
x.add(jd3)
x.add(jd2)
x.add(jd4)

x.view()