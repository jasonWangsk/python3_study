"""
多行文本框：text 控件
单行文本框： Entry 控件
都是使用tk库下面的控件对象
--
grid 布局
 类似Excel
 ipadx =  水平方向内边距
 ipady =  垂直方向内边距
 padx =  水平方向外边距
 pady =  垂直方向外边距
--
1 创建窗体
2 创建用户名/密码
3 创建文本框
4 创建按钮
5 登录后弹窗
"""
import tkinter
from tkinter import messagebox

def login():
    if enter_name.get() == "aaaa" and enter_pass.get() == "000000":
        win = tkinter.Tk()
        win.geometry("500x300+200+100")
        win.title("登录成功")
        lab = tkinter.Label(win, text="登录成功")
        lab.pack()
    else:
        messagebox.showinfo(title="弹窗提示", message="用户名或密码错误请重新输入!!")

def reset():
    new_name.set("")
    new_pass.set("")

# 创建登录窗体
win = tkinter.Tk()
win.title("登录demo")
# 设置高宽--位置居中一些
win.geometry("500x300+200+100")

"""
row 行索引
column 列索引
columnspan 列合并数量
rowspan 行合并数量
"""
# 创建标签
labname = tkinter.Label(win,text="用户名")
labname.grid(row=0,column=0,ipadx=10,ipady=10)  # 布局  0行 0列
# 创建行输入框
new_name = tkinter.StringVar()
enter_name = tkinter.Entry(win, textvariable=new_name)
enter_name.grid(row=0,column=1,columnspan=2) # 0行 1列 占2列

# 创建标签
labpass = tkinter.Label(win,text="密码")
labpass.grid(row=1,column=0) # 1行 0列

# 创建行输入框
new_pass = tkinter.StringVar()
enter_pass = tkinter.Entry(win,show="*", textvariable=new_pass)
enter_pass.grid(row=1,column=1,columnspan=2) # 1行 1列

# 创建登录按钮
button = tkinter.Button(win,text = "登录", width=5,command = login) #  按钮宽度width=5
button.grid(row=2,column=1)

# 创建重置 登录按钮
button_re = tkinter.Button(win,text = "重置",width=5,command = reset)
button_re.grid(row=2,column=2)


win.mainloop()


