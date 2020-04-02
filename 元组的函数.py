"""
tuple:
元组内的元素只能只读
"""
tup = (12,3,"11",12)
x = tup.index(12)
print(x)

x = tup.count(12)
print(x)

# 元组元素拼接 来扩展元组
tup2 = (0,55)
print(tup+tup2)

#使用元组索引来输出新元组
print((tup[1],tup2[0]))

# 删除 del 关键字
tu3 = (0,12,555,656)
# del tu3
print(tu3)
