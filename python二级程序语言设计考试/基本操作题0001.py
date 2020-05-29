

# 考查format()方法的格式控制
# 语法格式：  {参数序号:格式控制标记}
# 格式控制标记顺序包括：填充、对齐、宽度 ， .精度，类型
# ：后面带填充字符，只能是一个字符，默认空格
# s = input('输入一个字符串：')
s = 'python'
print("{:=>20}".format(s))  # 右对齐
print("{:=<20}".format(s))  # 左对齐
print("{:=^20}".format(s))  # 居中


# 循环结构考查
# 实现斐波那契数列 f(0)=0,f(1)=1 ,f(n) = f(n-1)+f(n-2)
a,b = 0,1
while a<=100:
    print(a,end='')
    a,b = b,a+b


# 海龟绘图
# 使用furtle.fd() 和 turtle.seth()函数绘制一个等边三角形
import turtle as t
for i in range(3):
    t.seth(i*120)
    t.fd(200)