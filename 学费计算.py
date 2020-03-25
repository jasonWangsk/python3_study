# 按学费一年10000，增长率1.05 计算10年后4年 学费总数

"""
# 第一种计算
money = 10000  # 初始值
for year in range(1,11):  # 循环十年每年递增
    money *= 1.05

money1 = money  # 第一年
money2 = money1 * 1.05
money3 = money2 * 1.05
money4 = money3 * 1.05

sum_4money = sum((money1,money2,money3,money4))
print(sum_4money)
"""

"""
# 第二种计算
money = 10000  # 初始值
for year in range(1, 11):  # 循环十年每年递增
    money *= 1.05

sum_4money = money
for year in range(1, 4):
    money *= 1.05
    sum_4money += money

print(sum_4money)
"""

"""
# 第三种计算
money = 10000
year = 1
while year < 11:
    money *= 1.05
    year += 1

year = 1
sum_4money = money
while year < 4:
    money *= 1.05
    year += 1
    sum_4money += money
print(sum_4money)
"""

# 第四种计算
money = 10000
year = 1
while True:
    if year < 11:
        money *= 1.05
        year += 1
    else:
        break

year = 1
sum_4money = money
while True:
    if year < 4:
        money *= 1.05
        year += 1
        sum_4money += money
    else:
        break
print(sum_4money)


