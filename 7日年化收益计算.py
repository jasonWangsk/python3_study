# 本金 * 7日年化收益率 = 预期一年收益
# 预期一年收益 / 365 = 每日收益
# 每日收益 /（本金/10000） = 每万份收益

money = input("请输入没本金：")
rate_of_return = input("请输入7日年化收益率：")
expected_oneyear_earnings = eval(money) * eval(rate_of_return)
print("预期一年收益",expected_oneyear_earnings)

every_day_earnings = expected_oneyear_earnings / 365
print("每日收益",every_day_earnings)

copies_10000 = every_day_earnings / (eval(money) / 10000)
print("每万份收益",copies_10000)
