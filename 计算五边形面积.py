import turtle
import math

# 多边形面积
# 五角形面积 = 五边形面积 = 5 * 边长*边长 / 4 * tan（派/边长）

side_length = input("请输入边长：")
side_length = eval(side_length)
# area = 5 * (side_length**2) / 4 * math.tan(math.pi/5)
area = 5 * (side_length**2) / math.tan(math.pi / 5) / 4


turtle.circle(side_length, steps = 5)
turtle.penup()
turtle.goto(0, side_length)
turtle.pendown()
turtle.write(round(area,2))

turtle.done()
