"""
@author: blake.wang
@file: study_08_Scale拉动条部件.py
@time: 2023/2/7 14:56 
"""
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')  # 这里的乘是小x

# 在图形界面上创建一个标签label用以显示并放置
l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()

v1 = tk.StringVar()


# 定义一个触发函数功能
def print_selection(text):
    # print(type(text))  # <class 'str'>
    print(f'text = {text}')
    # print(v1.get())
    # print(type(v1.get()))  # <class 'str'>
    l.config(text='you have selected ' + v1.get())


# 创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
s = tk.Scale(window, variable=v1, label='try me', from_=0, to=10, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2,
             resolution=0.01, command=print_selection)
s.pack()
print(v1.get())

# 主窗口循环显示
window.mainloop()
# https://blog.csdn.net/qiukapi/article/details/104068879
