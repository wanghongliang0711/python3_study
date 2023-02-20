"""
@author: blake.wang
@file: study_13_放置方式Pack.py
@time: 2023/2/20 14:45 
"""
import tkinter as tk

root = tk.Tk()
root.title("pack")
root.geometry("300x200")

l1 = tk.Label(root, text="left")
l1.pack(side=tk.LEFT)
l2 = tk.Label(root, text="right")
l2.pack(side=tk.RIGHT)
l3 = tk.Label(root, text="top")
l3.pack(side=tk.TOP)
l4 = tk.Label(root, text="bottom")
l4.pack(side=tk.BOTTOM)

root.mainloop()
# https://blog.csdn.net/weixin_42272768/article/details/100191059
