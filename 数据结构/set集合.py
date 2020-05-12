"""
set 中的数据不可以重合

"""
mylis = [1,1,1]
myset = {1,1,1}  # set 集合 中的数据不可以重合
print(mylis)
print(myset)
print(type(myset))

set1 = {1,2,3,4,5}
set2 = {1,2,3,6,7}
print(set1 - set2)  # 输出set1有 set2 没有的  差集
print(set2 - set1)  # 输出set2有 set1 没有的

# 并集
print(set1 | set2)

# 交集
print(set1 & set2)

print(set1 ^ set2)  # 并集- 交集