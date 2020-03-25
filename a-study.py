# 99 乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j} = {i*j}', end=' ')
    print()

for k in [2, 3, 5, 6, 7]:
    if k == 6:
        continue
    print(k)

# 字符串 切片 [开始:结束(不包含结束):步长]
ss = "床前明月光！"

print(ss[0::2])

print(f"测试之家账户{ss}哈哈哈哈")

filel = open('aaa-test.txt', mode='w', encoding='utf-8')
filel.write('787878\n')
filel.write('哈哈哈哈')
filel.close()
