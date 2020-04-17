"""
：任一大于2的整数都可写成三个质数之和
 质数是指在大于1的自然数中，除了1和它本身以外不能被其他自然数整除的数叫做质数
 只能被1 和 它本身整除叫质数
举例：
 拆分任意偶数 = 2个质数之和
"""


def judge_num(num):
    """判断传入参数为质数"""
    if num < 0:
        return False
    elif num == 0 or num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        isdata = True  # 假定是质数，判断10
        for i in range(2, num):  # 判断2-9
            if num % i == 0:  # 假如有一个被整除 跳出循环
                isdata = False
                break
        return isdata


def cf(num):
    """拆分"""
    for i in range(1, num):
        if judge_num(i) and judge_num(num - i):
            print(f"{num} = {i}+{num - i}")


cf(34)
