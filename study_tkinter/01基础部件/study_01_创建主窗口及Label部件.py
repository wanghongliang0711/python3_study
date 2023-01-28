"""
@author: blake.wang
@file: study_01_创建主窗口及Label部件.py
@time: 2023/1/28 20:11 
"""
import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()
window.configure(background='gray')  # 设置窗体的背景颜色
# 第2步，给窗口的可视化起名字
window.title("My Window")

# 第3步，设定窗口的大小和位置(长 * 宽 + 距离左屏幕距离 + 距离上屏幕距离)
window.geometry("500x300+100+200")  # 这里的乘是小x，也可以写为 "+100+200"不设置窗口大小

# 第4步，在图形界面上设定标签
l = tk.Label(window, text="hello world，你好世界", bg='green', font=('Arial', 12), width=30, height=2)

# 第5步，放置标签  放置lable的方法有：1）l.pack(); 2)l.place();
l.pack()  # Label内容content区域放置位置，自动调节尺寸

# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
