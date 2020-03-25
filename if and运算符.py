num1 = 10
num2 = 0
num3 = 23

a = (num1 >num3>num2)

b = (num2 <num3)

c = (num3 < num1)


# and 条件里所有都要满足
if a and b and c:
    print(True)
else:
    print(False)