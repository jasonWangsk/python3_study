# !usr/bin/env python3
"""
使用in判断元素是否在序列中
"""



list_data = [
    ["aaa","111"],
    ["bbb","222"]
]
username = input("请输入用户名：")
pw = input("请输入密码：")

if [username,pw] in list_data:
    print("恭喜登录系统成功！！！")
else:
    print("输入错误！！请检查用户名或密码!")