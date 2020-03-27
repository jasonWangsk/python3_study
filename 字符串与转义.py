"""
字符串为单引号或双引号中的文本或字符
给变量赋值为字符串类型，第二次赋值会覆盖第一次的赋值
 可以单双引号互相嵌套使用
"""
x = "1"
x = "2"
print(x)

y = ' "哈哈哈" '
print(y)
z = " '090909' "
print(z)

# 转义符为:\,  \n 换行符号， \t 制表符
u = "kjkjk\http://aaa.cn"
u = 'kjkjk\"http://aaa.cn\"'
u = 'kjkjk\n"http://aaa.cn\"'
u = 'kjkjk\\n"http://aaa.cn\"' # 取消转义 \\
print(u)

# 字符串前 + r  取消转义
print(r'kjkjk\n"http://aaa.cn\"')

# 使用repr函数 输出有单引号，注意长度包含来引号！
k = 'kjkjk\n"http://aaa.cn\"'
print(repr(k))

# 字符串拼接