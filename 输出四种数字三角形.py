"""
1
1 2
1 2 3
1 2 3 4
。。。。。。
"""
num = 6
r = 0
while r < num:
    for j in range(r+1):
        print(j+1, end=" ")
    print()
    r +=1

print("----------------------------")
"""
。。。。。。
1 2 3 4
1 2 3
1 2
1
"""
num = 6
while num > 0:
    for i in range(num):
        print(i+1,end=" ")
    print()
    num -=1