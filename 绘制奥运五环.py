import turtle
# 奥运五环

turtle.color('blue')
turtle.circle(100)   # 半径 100

turtle.penup()  # 抬起笔
turtle.goto(-200,0) # 移动坐标位置
turtle.pendown()    # 放下笔
turtle.color('red')
turtle.circle(100)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.color('orange')
turtle.circle(100)


turtle.penup()
turtle.goto(100,-200)
turtle.pendown()
turtle.color('black')
turtle.circle(100)

turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.color('green')
turtle.circle(100)


turtle.done() # 程序继续执行

