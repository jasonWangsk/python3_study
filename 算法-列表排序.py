"""
python 列表和数组都区别
：列表中都数据类型不必相同，而 array中的类型必须全部相同
"""

# 使用内置函数sorted（）直接排序
arr = [64, 34, 25, 12, 22, 11, 90]
print(sorted(arr))  # 默认升序
print(sorted(arr, reverse=True))  # 使用reverse关键字降序

# 冒泡排序
# 排序的根本思想：本质上是数值的比较
# 数值比较的本质：两两比较
# len()方法 返回对象（列表，元组、字符串）个数或长度

print("""---------------------""")

def maopao_sort(*n, sequence="a"):
    t = list(n)  # 输入参数转换成list
    for i in range(len(t)):  # 从列表第0个元素开始取值，这一层循环表示多少轮，每轮取一个值
        for j in range(i + 1, len(t)):  # 从列表的第2个元素开始
            if sequence == "a":  # 默认值从大到小排序
                if t[i] > t[j]:
                    t[i], t[j] = t[j], t[i]  # 如果大于就进行交换 否则不交换
            else:  # 否则从大到小排序
                if t[i] < t[j]:
                    t[i], t[j] = t[j], t[i]

    return t

# print(maopao_sort(5, 34, 10, 6, 8, 0, 3, sequence="a"))

print("""---------------------""")
l1 = [99, 101, 23, 33, 46, 98, 76]
for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

print("""---------------------""")
list_data = [23,12,3,54,10,9,0]
#第一步从0开始遍历列表中元素的数量或长度
for i in range(len(list_data)):
    # 第二步 从i+1开始遍历列表中的元素个数
    for j in range(i+1,len(list_data)):
        # 比较列表中第i个和第j个元素大小
        if list_data[i] > list_data[j]:
            # 如果大于两个元素进行交换
            list_data[i],list_data[j] = list_data[j],list_data[i]
print(list_data)


