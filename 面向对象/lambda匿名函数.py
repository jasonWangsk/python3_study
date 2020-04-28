"""
匿名函数
"""

(lambda mystr: print(mystr))("helloword")

x = lambda a,b,c:a+b*c
print(x(1,2,3))