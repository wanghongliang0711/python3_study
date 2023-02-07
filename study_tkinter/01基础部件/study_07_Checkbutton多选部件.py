"""
@author: blake.wang
@file: study_07_Checkbutton多选部件.py
@time: 2023/2/7 14:12 
"""
import tkinter as tk

window = tk.Tk()
window.title("Checkbutton多选")
window.geometry("500x300")

# 在图形界面上创建一个标签label用以显示并放置
l = tk.Label(window, bg='yellow', width=40, text='empty')
l.pack()


def print_selection():
    temp_list = ["", "", ""]
    temp_list[0] = "Python" if var1.get() == 1 else "not Python"
    temp_list[1] = "C++" if var2.get() == 1 else "not C++"
    temp_list[2] = "Java" if var3.get() == 1 else "not Java"
    l.config(text=str(temp_list))


# 定义3个Checkbutton选项并放置
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)    # 传值原理类似于radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='Java',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()

window.mainloop()
# https://blog.csdn.net/weixin_42272768/article/details/100626806
