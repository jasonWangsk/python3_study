# 贷款计算公式
"""
月供 = 贷款总额  * 月利率 / 1 - （1 / （1 + 月利率）** （年限 * 12））
"""

loan_year = eval(input("请输入贷款年限："))
loan_money = eval(input("请输入贷款金额："))
month_rate = eval(input("请输入贷款月利率："))

month_payment = (loan_money * month_rate) / (1 - 1 / (1 + month_rate) ** (loan_year * 12))
all_paypemnt = month_payment * 12 * loan_year
print("月供：", round(month_payment, 2))
print("月供：", round(month_payment, 3))
print("总还款额：", all_paypemnt)
