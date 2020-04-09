import tkinter
from tkinter import messagebox


def view():
    '''弹出对话框'''
    tkinter.messagebox.showinfo("哈哈哈哈哈","http://xxxxxxxxx")


win = tkinter.Tk()  # 创建窗体
win.title("窗口开发")
win.geometry("960x450")  # 宽x高
# 创建标签 ，文本存放在win窗体里
label = tkinter.Label(win, text = "python3 编程")
label.pack()

# 创建按钮
print()
button = tkinter.Button(win, text = "点击查看信息", command = view)
button.pack()
win.mainloop()  # “”“运行Tcl的主循环。”“”
