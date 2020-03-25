# 所有二元运算符都是从左到右都结合顺序
# 一元运算： 正负
# 二元运算： 加减法
print(1+2*2/3>2*(3-2)+1) # 不规范写法

print((1+2*2/3) > (2*(3-2)+1))  # 符号软件工程规范


# and优先级 高于 or
# and优先级 高于 or
# and优先级 高于 or


print(True or True and False)
print(True and True or False)
print(True or False)
print(True and False)
