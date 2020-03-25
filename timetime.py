import time

mytimes = time.time()
print(f"自从1970到现在过去了 {int(mytimes)} 秒")
seconds = int(mytimes)%60
hours = int(mytimes)// 3600
print(hours)
mints = int(mytimes)-int(mytimes)//3600*3600
mins = (mints-seconds)

print(f"自从1970到现在过去了"
      f"{hours} 小时,{mins} 分, {int(seconds)} 秒")