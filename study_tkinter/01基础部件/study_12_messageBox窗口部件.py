"""
@author: blake.wang
@file: study_12_messageBox窗口部件.py
@time: 2023/2/20 14:15 
"""
import tkinter as tk
import tkinter.messagebox


window = tk.Tk()
window.title("messageBox")
window.geometry("500x300")


# 定义触发函数功能
def hit_me():
    # tk.messagebox.showinfo(title='Hi', message='你好！')
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'


tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

window.mainloop()
