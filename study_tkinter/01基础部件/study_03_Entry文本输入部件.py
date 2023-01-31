"""
@author: blake.wang
@file: study_03_Entry文本输入部件.py
@time: 2023/1/31 8:43 
"""
import tkinter as tk

window = tk.Tk()

window.title("My Window")

window.geometry("500x300+100+200")

# 在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(window, show="*", font=('Arial', 14))  # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e3 = tk.Entry(window, show="5", font=('Arial', 14))  # 所有输入显示成5

e1.pack()
e2.pack()
e3.pack()


def print_e2():
    global e2
    print(e2.get())


# 点击按钮获取 e2 输入的内容
bt1 = tk.Button(window, text="print e2", font=("Arial", 12), width=15, height=1, command=print_e2)
bt1.pack()

window.mainloop()
