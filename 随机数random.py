"""
random.randint(a,b)  可以用来产生一个a和b之间且包括a和b
的随机整数
random.randrange(0, 10)  生成0 - 9 不包含10
"""

import random

print(random.randint(1,3))

print(random.randrange(1,3))
print(random.random())
print(random.choice("01234"))