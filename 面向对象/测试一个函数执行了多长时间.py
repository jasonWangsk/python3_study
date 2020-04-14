import time

def times(parameter):
    """时间差"""
    start_t = time.time()
    parameter()  # 函数参数
    end_t =time.time()
    times = end_t - start_t
    print(times)

def func1():
    num = 0
    for i in range(1,100000000):
        num+=i
    print(num)

def func2():
    num = 0
    for i in range(1,10000):
        num+=i
    print(num)

# times(func1)
# times(func2)


# nonlocal 函数内层变量全局化
def fun1():
    num = 5
    def fun2():
        nonlocal num
        # global num
        num = 6
        print("fun2:",num)
    fun2()
    print("fun1:",num)
fun1()

