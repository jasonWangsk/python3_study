"""
字符串后使用 .find()函数

"""

import codecs

file = codecs.open("/Users/tester/Desktop/python3_study/aa.txt", "rb", "utf-8", "ignore")
# 参数说明：第一个路径，第二个rb二进制读取，第三个参数汉字编码，第四个忽略错误
linestr = file.readlines()  # 读取一行
while True:
    names = input("输入名称：")
    for line in linestr:
        if line.find(names) != -1:
            print(linestr)
        if line == None:
            break
