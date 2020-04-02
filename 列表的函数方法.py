"""
列表的函数
"""

# count() 统计元素在列表中的个数
list1 = [1,22,23,22,45,"a","b"]
print(list1.count(22))
print(list1)

# copy()  “”“返回列表的浅表副本。”“”
list2 = list1.copy()
list2[0] = "哈哈哈哈哈"
print(list2)

# index()  元素 在列表中索引位置

# reverse 逆序从组 ，
list1.reverse()
print(list1)

# sort 默认正向排序
list2 = [78,1,22,23,22,45]
list2.sort()  # 默认升序
print(list2)

list2.sort(reverse=True)  # reverse=True 降序
print(list2)

# sorted 排序
x = sorted(list2)  # 默认升序
print(x)

x = sorted(list2,reverse=True)  # reverse=True 降序
print(x)

