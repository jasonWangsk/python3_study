# 字符串//数组 切片 [开始:结束(不包含结束):步长]
# [:] 读取全部
# [x:] 从x到最后读取 [:x] 从头到x读取
# [-1:-2]  逆向读取
ss = "床前明月光!"
x = ss[1:3]     # 开始:结束(不包含结束)
print(x)
x = ss[:3]
print(x)

print(ss[1::3]) # [开始:结束(不包含结束):步长]

print(f"测试之家账户{ss}哈哈哈哈")

filel = open('aaa-test.txt', mode='w', encoding='utf-8')
filel.write('787878\n')
filel.write('哈哈哈哈')
filel.close()

# 使用步长读取奇偶数
i = [1,2,3,4,5,6,7,8,9,10]
print("偶数有：", i[1::2])
print("奇数数有：", i[0::2], end=" ")


