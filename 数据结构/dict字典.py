"""
字典是set集合的升级 key不允许重复
{key: value}
"""

dic1 = {"123":20,"jj":0,"123":14}
dic2 = {"123":20,"ll":20}
print(dic2)
print(dic2["ll"])

# 循环字典

for key in dic2:
    print(key,dic2[key])