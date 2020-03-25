import turtle


turtle.screensize(1024,1024)  # 设置屏幕大小

# 画三角形
turtle.pensize(5)  # 设置画笔宽度
turtle.circle(100,steps = 3)  # steps 边的数量

# 颜色填充
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.begin_fill()  # 开始填充
turtle.circle(100,steps = 3)
turtle.color("blue")
turtle.end_fill()  # 结束填充

# 颜色填充2
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()  # 开始填充
turtle.circle(100,steps = 3)
turtle.color("red")
turtle.end_fill()  # 结束填充

turtle.hideturtle()  # 隐藏画笔箭头


turtle.done()
