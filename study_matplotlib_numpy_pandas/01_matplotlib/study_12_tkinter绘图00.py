"""
@author: blake.wang
@file: study_12_tkinter绘图00.py
@time: 2023/1/27 14:45 
"""
import tkinter as tk




def main():
    root = tk.Tk()
    root.configure(background='gray')
    root.geometry("+10+10")
    # frameRightWindow = tk.Frame(root)
    canvas = tk.Canvas(root, width=300, height=300,
                       borderwidth=40,
                       highlightbackground='white', bg='gray')
    canvas.grid(row=0, column=0, columnspan=3)
    root.mainloop()



if __name__ == '__main__':
    main()