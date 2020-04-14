"""
python中没有接口的概念
接口：实际上是定义一个 规范
接口的实现：通过具体继承这个接口的类来实现
通过 hasattr(类对象，类方法)，来判断类中是否有对应的方法，有返回true 否则 false
    参数1：类对象
    参数1：类方法/属性
getattr()

"""
import random
import json
class City:

    def __init__(self):
        """初始化城市属性"""
        self.city_name = input("cityName:")
        self.city_weather = input("city_weather:")
        # self.city_province = input("city_province:")
        self.city_code = random.randint(1001,9999)

    def return_city(self):
        param = {
            "city_code": self.city_code,
            "city_name": self.city_name,
            "city_weather": self.city_weather
        }
        return param

c = City()
x = json.dumps(c.return_city(),ensure_ascii=False)
print(x)
# print(c.return_city())