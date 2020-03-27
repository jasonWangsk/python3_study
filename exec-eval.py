"""
exec 执行储存在字符串或文件中的 Python 语句
exec(object[, globals[, locals]])
参数1： 字符串或代码对象。
参数2：可选。包含全局参数的字典。


"""
# 参数:字符串


x = 'name = "Bill"\nprint(name)'
exec(x)

i = 12
j = 13
result = "answer=i*j\nprint(answer)"
exec(result)

num1 = 100
num2 = 200
exec("num = num1*num2\nprint(num)")



# 参数：代码对象
persin_obj = {"name":"老王", "age": "23"}
exec("print('姓名:'+name ,'年龄:' + age)",persin_obj)


