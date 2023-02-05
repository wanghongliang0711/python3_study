"""
@author: blake.wang
@file: study_05_Listbox列表框部件.py
@time: 2023/2/5 18:14 
"""
import tkinter as tk

window = tk.Tk()

window.title("Listbox")

window.geometry("500x300")

# 在图形界面上创建一个标签label用以显示
var1 = tk.StringVar()
l = tk.Label(window, bg="green", fg="yellow", font=('Arial', 12), width=10, textvariable=var1)
l.pack()


# 创建一个方法用于按钮的点击事件
def print_selection():
    select_index = lb.curselection()  # 获取当前选中的文本下标
    tmp = ""
    for i in select_index:
        tmp = tmp + str(lb.get(i))
    # value = lb.get(lb.curselection())   # 获取当前选中的文本
    var1.set(tmp)  # 为label设置值
    # lb.selection_clear(0, 10)  # 清除 0~10 index之间的选择
    # lb.selection_clear(0)  # 清除 index为 0 的选择


# 创建一个按钮并放置
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set((1, 2, 3, 4))  # 为变量var2设置值
# https://blog.csdn.net/m0_37264397/article/details/79079259
# lb = tk.Listbox(window, listvariable=var2, width=20, height=10)  # 单选
lb = tk.Listbox(window, selectmode=tk.MULTIPLE, listvariable=var2, width=20, height=10)  # 多选
lb.pack()

list_items = [11, 22, 33, 44]
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置开始加入值

lb.insert(1, 'first')  # 在第一个位置加入'first'字符
lb.insert(2, 'second')  # 在第二个位置加入'second'字符
lb.delete(2)  # 删除第二个位置的字符

window.mainloop()
