"""
@author: blake.wang
@file: study_04_Text多行文本输入部件.py
@time: 2023/2/5 17:42 
"""
import tkinter as tk

window = tk.Tk()

window.title('Text Test')

window.geometry("500x300")

e = tk.Entry(window, show = None) #显示成明文形式
e.pack()

# 定义两个触发事件时的函数insert_point和insert_end
def insert_point():  # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert("insert", var)

def insert_end():
    var = e.get()
    t.insert("end", var)

def clear_text():  # https://blog.csdn.net/weixin_43097301/article/details/84206539
    # t.delete(1.0, tk.END)  # index1 从1开始，1.0 代表第一行的第0个元素，tk.END代表结尾
    t.delete(1.0, 3.0)

b1 = tk.Button(window, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()
b3 = tk.Button(window, text='clear_text', width=10,
               height=2, command=clear_text)
b3.pack()


t = tk.Text(window, height = 3)
t.pack()

window.mainloop()
