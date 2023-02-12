"""
@author: blake.wang
@file: study_09_Canvas画布部件.py
@time: 2023/2/7 15:15 
"""
import tkinter as tk

window = tk.Tk()
window.title("Canvas画布")
window.geometry("500x300")

# 在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg="green", height=200, width=500)
# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='pic.gif')  # 图片位置，图片像素太大会导致显示不全
# anchor : n, ne, e, se, s, sw, w, nw, or center
image = canvas.create_image(250, 0, anchor='n', image=image_file)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处

# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)  # 画直线 https://blog.csdn.net/weixin_42272768/article/details/100852360
# oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
oval = canvas.create_oval(220, 150, 270, 200, fill='yellow')  # https://blog.csdn.net/weixin_42272768/article/details/100864851
canvas.create_oval(0, 50, 50, 0, fill='yellow')  # 画圆的原理是先用两个点确定一个长/正方形，然后在长/正方形里面画出圆或者椭圆
canvas.create_line(0, 50, 50, 0)
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=290)  # 画扇形 从0度打开收到290度结束，和画圆的原理一样
canvas.create_line(x0, y0+50, x1, y1+50)
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)  # 画矩形正方形  https://blog.csdn.net/weixin_42272768/article/details/100873319
canvas.pack()

canvas_text = canvas.create_text(250, 140, text="会当凌绝顶一览众山小",  fill='red', font=('verdana', 20))


# 触发函数，用来移动指定图形
def moveit():
    canvas.move(rect, 2, 2)  # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动


def update_text():
    canvas.itemconfigure(canvas_text, text="*****888******")


b = tk.Button(window, text='move item', command=moveit).pack()
b1 = tk.Button(window, text='update text', command=update_text).pack()

window.mainloop()
# https://blog.csdn.net/weixin_42272768/category_9315268.html
# https://blog.csdn.net/weixin_42272768/article/details/100852283
# https://blog.csdn.net/weixin_42272768/article/details/100852360
