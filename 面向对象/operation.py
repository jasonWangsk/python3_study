"""
工资标准 a = 10000
基本工资 a = 10000

工资标准（100） = 基本工资 50% + 房补 13% + 月奖金标准 37%


工作天数  b = 30
学历  本科 c =
加薪  0  d = 0
加班  0  e = 0
事假扣款  f = (基本工资 + 房补 + 月奖金标准)/30 * 事假总天数
病假扣款  g = 基本工资/30*病假天数*病假基本工资扣除系数 + （房补 +月奖金标准 ）/ 30 * 病假天数
迟到 0
违纪 0
其他 1

本月应发 = 基本工资 + 房补 + 月奖金标准 + 学历 + 加薪 +加班 - 事假扣款 -病假扣款 - 其他

社保费  基本工资 * 8%

所得税

合计代扣 = 保险费 + 所得税

实际应发 = 本月应发 - 合计代扣







"""





def work_days():
    pass

def gongzibiaozhun():
    """
    工资标准（100） = 基本工资 50% + 房补 13% + 月奖金标准 37%

    :return:
    """
    pass

def xueli():
    """学历"""
    pass

def jiaxinbucha():
    """加薪补差"""
    pass

def jiabangongzi():
    """加班工资"""
    pass

def shijiakoukuan():
    """事假扣款"""
    pass

def bingjiakoukuan():
    """病假扣款"""
    pass

def benyueyingfa():
    """本月应发"""
    pass

def hejidaikou():
    """合计代扣"""
    pass

def shifagongzi():
    """实发工资"""
    pass


import jieba

lis_s = '实发工资合计代扣'
x = jieba.lcut(lis_s)
print(x)
y = jieba.lcut_for_search(lis_s)
print(y)