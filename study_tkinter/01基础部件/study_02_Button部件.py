"""
@author: blake.wang
@file: study_02_Button部件.py
@time: 2023/1/30 20:07 
"""
from functools import partial
import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()
window.configure(background='gray')  # 设置窗体的背景颜色
# 第2步，给窗口的可视化起名字
window.title("My Window")

# 第3步，设定窗口的大小和位置(长 * 宽 + 距离左屏幕距离 + 距离上屏幕距离)
window.geometry("500x300+100+200")  # 这里的乘是小x，也可以写为 "+100+200"不设置窗口大小

# 第4步，在图形界面上设定标签
label_text = tk.StringVar()  # # 将label标签的内容设置为字符类型，用label_text来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=label_text, bg='green', fg="white", font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():  # 传参方式一使用全局变量
    global on_hit, label_text
    if on_hit is False:
        on_hit = True
        label_text.set("hello world")
    else:
        on_hit = False
        label_text.set("")

def hit_me2(label_text):  # 传参方式二：https://zhuanlan.zhihu.com/p/475384940
    if label_text.get() == "":
        label_text.set("hello world")
    else:
        label_text.set("")

# 第5步，在窗口界面设置放置Button按键
bt1 = tk.Button(window, text="hit/show label text 1", font=("Arial", 12), width=15, height=1, command=hit_me)
bt2 = tk.Button(window, text="hit/show label text 2", font=("Arial", 12), width=15, height=1, command=partial(hit_me2, label_text))
bt3 = tk.Button(window, text="hit/show label text 3", font=("Arial", 12), width=15, height=1, command=lambda: hit_me2(label_text))
bt1.pack()
bt2.pack()
bt3.pack()

# 第6步，主窗口循环显示
window.mainloop()