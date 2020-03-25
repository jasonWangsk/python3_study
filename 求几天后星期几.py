# 计算n天后周几？

while 1:
    today = input("今天周几：")
    n = input("n天后：")
    n = eval(n)
    future_day = (eval(today)+n) % 7
    if  future_day == 0:
        future_day = "日"

    print(f"{n}天后是星期{future_day}")
    print("%d天后是星期%s" % (n,future_day))
    print(n,"天后是星期",future_day)