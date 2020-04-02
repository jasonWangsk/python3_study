"""
[
[1,2,3],
[4,5,6],
[8,2,9]
]
互换
[
[1,4,7],
[2,5,8],
[3,6,9]
]


"""
lis = []
k = 1
for i in range(3):
    num=[]
    for j in range(3):
        num.append(k)
        k+=1
    lis.append(num)
# print(lis)

lit = []
lit2 = []
s = 0
for i in range(3):
    s+=1
    lit.append(s)
lit2.append(lit)
print(lit2)


tbox_d = ["121212","789789"]
y = "456"
for i in range(len(tbox_d)):
    for j in range(i+1,len(tbox_d)):
        if y in tbox_d[i]:
            print(y)
        else:
            y = tbox_d[j]
            print(y)
