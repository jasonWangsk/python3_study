
# 99 乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j} = {i*j}', end=' ')
    print()

for k in [2, 3, 5, 6, 7]:
    if k == 6:
        continue
    print(k)
