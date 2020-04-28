"""
循环遍历一个自动定义实数范围的小数
"""

#  使用for 循环来实现循环遍历小数

x = [i/100.0 for i in range(10,50)]  # 0.1--0.49
y = [i/1000.0 for i in range(10,50)]  # 0.01--0.049
print(x)
print(y)

# 使用numpy
import numpy as np
z = np.arange(0.1,0.5,0.01)  # 0.1--0.49
k = np.arange(0.01,0.05,0.001)  # 0.01--0.049

print(k)