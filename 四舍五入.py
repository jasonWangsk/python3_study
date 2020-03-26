# round() 方法
# 四舍五入
num = 11.25
print(round(num))

num = 11.56
print(round(num))

# 保留小数点后 n 位数

num = 11.256823
print(round(num,3))
print(round(num,2))

# 拆分成元角分输出
money = 110.567
print(int(money),"元")
print(int(money * 10) % 10,"角")
print(int(round(money * 100) % 10),"分")
print(9%6)

# 引入decimal模块 计算实数的精度
# 使用 decimal下的 Context函数中的参数prec（用来显示最终的数值，长度包含整数位和小数位）
# 和rounding参数 赋值decimal.ROUND_HALF_UP算法 计算四舍五入
# create_decimal函数 参数传入字符串
import decimal
x = 123.4554
y = decimal.Decimal(x)
print(y)

# 在context 环境下场景一个decimal实例
a = decimal.Context(prec=8,rounding=decimal.ROUND_HALF_UP).create_decimal(str(x))  # prec=取值包含整数位
print(a)

# 四舍五入
a = round(x,2)
print(a)
