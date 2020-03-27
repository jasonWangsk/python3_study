"""
> < >= <= == !=

is is not
in not in

字符串比较（ascii 比较，长短比较）


== 比较的是对象中的值
is 比较的是整个对象区域
in

"""

x = 1
y = [2,3]

if x in y:
    print(True)
elif x not in y:
    print(False)


x = "a"
y = "apple"

if x in y:
    print(True)
elif x not in y:
    print(False)



x = 1
y = 2
if x is y:
    print(True)
elif x is not y:
    print(False)


x = {"key": "apple"}
y = {"key": "apple"}
print(x == y)



x = (1,2,3)
y =  (1,2,3)
print(x is y)
print(x == y)

