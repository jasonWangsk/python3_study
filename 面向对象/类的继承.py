"""
B继承A
B是子类，A是父类
"""

class A:
    def chifan(self):
        print("爱吃饭")

class B:
    def shuijiao(self):
        print("爱睡觉")

class C(A,B):
    def hejiu(self):
        print("爱喝酒")

# result = B()
# result.chifan()
# result.shuijiao()

result2 = C()
result2.shuijiao()
result2.hejiu()
result2.chifan()

