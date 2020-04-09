from math import pi

x = "pi={}"
print(x.format(pi))

y = "pi={0},pi2={0}"
print(y.format(pi))

# 字符串 保留2位小数 及换行
y = "pi={0}\npi2={0:.2f}"
print(y.format(pi))

# 默认右对齐补零  0:015
# < 做对齐， > ， ^ 居中对齐
y = "pi={0}\npi2={0:^015.2f}"
print(y.format(pi))


s = "{a}欢迎{b}访问{c}系统!!!"
print(s.format(a="你好",b="王总",c="哈哈哈哈哈哈"))