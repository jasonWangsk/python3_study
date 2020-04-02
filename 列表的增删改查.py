"""
分别使用：
+
分片技术
append()
insert()
expand

"""
"""
列表元素增加
"""
# +
l1 = ["a","b",1]
l2 = ["c","d"]
print(l1+l2)
l3 = l1+l2
# 切片截取字符串
abc = l3[0:2] + l3[3:4]
print(abc)
# 使用切片插入数据
l1[2:2] = "c","d","e"
print(l1)


# 使用insert（）插入数据
l4 = [1,2,3,4]
l4.insert(4,5)
print(l4)

# 使用append()追加
l4.append(6)
print(l4)

# 使用extend()  “”“通过添加可迭代的元素来扩展列表。”“”
l4.extend("?")
l4.extend((666,999))

print(l4)

"""
列表元素删除
"""
del l4[0]   # del 关键字按照元素 索引 删除
print(l4)

# remove()
l4.remove("?")  # 参数为列表元素
print(l4)

# pop()  删除并返回索引处的项目（默认为最后一个）。
l4.pop()  # 参数为 元素索引或为空
print(l4)

# 清空 clear()
# l4.clear()
# print(l4)

"""
列表元素修改
"""
# 直接赋值
l4[0] = 123
print(l4)

# 切片方法修改或增加
l4[0:2] = ["a","b"]
print(l4)

print(l4.count(" "))

