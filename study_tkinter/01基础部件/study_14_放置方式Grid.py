"""
@author: blake.wang
@file: study_14_放置方式Grid.py
@time: 2023/2/20 14:45 
"""
import tkinter as tk

root = tk.Tk()
root.title("grid")
root.geometry("300x200")

b1 = tk.Label(root,text='跨\n两\n列',bg='blue')
b1.grid(row=0,column=0,rowspan=2)
b2 = tk.Label(root,text='跨两行',bg='yellow')
b2.grid(row=0 ,column=1,columnspan=2)
b3 = tk.Label(root,text='文本3',bg='cyan')
b3.grid(row=1,column=1)
b4 = tk.Label(root,text='文本4',bg='cyan')
b4.grid(row=1,column=2)

root.mainloop()
# https://blog.csdn.net/weixin_42272768/article/details/100191059
