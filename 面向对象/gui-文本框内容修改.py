import tkinter


name_var = "您好 %s，欢迎使用~!~!~!"
def modify():
    text_v.set(name_var % (text_box.get()))

win = tkinter.Tk()
win.geometry("450x200")

# 创建单行文本框
text_box = tkinter.Entry(win)
text_box.grid(row=1,column=1, padx=5)
# 创建按钮
button = tkinter.Button(win,text="修改",width=5,command = modify)
button.grid(row=1,column=5)
# 创建和绑定标签的控件变量对象
text_v = tkinter.StringVar()
text_v.set(name_var % (""))
text_str = tkinter.Label(win, textvariable = text_v)
text_str.grid(row=2,column=1)


win.mainloop()
