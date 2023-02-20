"""
@author: blake.wang
@file: study_15_放置方式Place.py
@time: 2023/2/20 14:45 
"""
import tkinter as tk

root = tk.Tk()
root.title("place")
root.geometry("300x240")

t = tk.Frame(root,width=280,height=230)
b1 = tk.Canvas(t,bg='blue',width=40,height=80)
b1.place(x=0,y=0, anchor='nw')  # anchor默认值是nw。n, ne, e, se, s, sw, w, nw, or center
b2 = tk.Canvas(t,bg='yellow',width=80,height=40)
b2.place(x=55,y=10)
b3 = tk.Canvas(t,bg='cyan',width=40,height=40)
b3.place(x=10,y = 100)
b4 = tk.Canvas(t,bg='gray',width=40,height=40)
b4.place(x=110,y=100)
t.place(x=0,y=0)

root.mainloop()
# https://blog.csdn.net/weixin_42272768/article/details/100191059
