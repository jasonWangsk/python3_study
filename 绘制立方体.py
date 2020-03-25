import turtle

# 画第一个正方形
turtle.write('0,0')
turtle.goto(0,200)
turtle.write('0,200')
turtle.goto(200,200)
turtle.write('200,200')
turtle.goto(200,0)
turtle.write('200,0')
turtle.goto(0,0)

# 画第二个正方形

turtle.penup()
turtle.goto(100,100)
turtle.pendown()

turtle.write('100,100')
turtle.goto(100,-100)
turtle.write('100,-100')
turtle.goto(-100,-100)
turtle.write('-100,-100')
turtle.goto(-100,100)
turtle.write('-100,100')
turtle.goto(100,100)

# 画连接线
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.goto(-100,100)

turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.goto(100,100)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.goto(100,-100)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-100,-100)








turtle.done()