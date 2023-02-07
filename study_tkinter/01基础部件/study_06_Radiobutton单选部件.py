"""
@author: blake.wang
@file: study_06_Radiobutton单选部件.py
@time: 2023/2/7 13:25 
"""
import tkinter as tk

window = tk.Tk()
window.title("Radiobutton")
window.geometry("500x300")

# 在图形界面上创建一个标签label用以显示并放置
var = tk.IntVar()  # 这里要用 IntVar()。经过测试如果用StringVar() 当没设设置默认值时，默认会全部选中
l = tk.Label(window, bg="yellow", width=20, text='empty')
l.pack()


# 定义选项触发函数功能
def print_selection():
    l.config(text='you have selected ' + str(var.get()))


# 创建三个radiobutton选项，其中variable=var, value=1的意思就是，当我们鼠标选中了其中一个选项，把value的值1放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, value=1, command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value=2, command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value=3, command=print_selection)
r3.pack()


window.mainloop()
# https://blog.csdn.net/weixin_42272768/article/details/100607621
