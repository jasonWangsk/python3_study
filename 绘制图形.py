import turtle

turtle.screensize(1024,768)  # 设置屏幕大小
turtle.showturtle()
turtle.circle(100)  # 半径100 的圆

turtle.penup()
turtle.goto(100,200)
turtle.pendown()
turtle.write("hellp python",font=("花文琥珀",50,"normal"))  # 设定字体大小


turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.circle(200,steps = 3)  # steps 边的数量

# 颜色填充
turtle.begin_fill()  # 开始填充
turtle.circle(200,steps = 5)  # 五边形
turtle.color("blue")
turtle.end_fill()  # 结束填充

# turtle.reset()  # 重置
turtle.begin_fill()
turtle.color("black")
turtle.pensize(10)  # 设置画笔宽度
turtle.circle(200,steps = 4)
turtle.color("red")
turtle.end_fill()

turtle.hideturtle()  # 隐藏画笔箭头


turtle.done()
