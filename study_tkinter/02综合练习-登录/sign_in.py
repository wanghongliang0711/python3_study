"""
@author: blake.wang
@file: sign_in.py
@time: 2023/2/23 16:35 
"""
import tkinter as tk
import tkinter.messagebox
import os
import pickle

window = tk.Tk()

window.title("登录")
window.geometry("400x300")
# window.configure(bg='gray')

# 加载欢迎图片
my_canvas = tk.Canvas(window, width=400, height=115, bg="green")
image_file = tk.PhotoImage(file='pic.gif')
image = my_canvas.create_image(200, 0, anchor='n', image=image_file)
my_canvas.pack(side='top')
tk.Label(window, text="Welcome", font=('Arial', 16)).pack()

# 用户名、密码 Label
tk.Label(window, text="User name:", font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text="Password:", font=('Arial', 14)).place(x=10, y=210)

# 用户登录输入框entry
# 用户名
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120, y=175)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120, y=215)


# 定义用户登录功能
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    usr_file_path = os.path.join(os.getcwd(), "usrs_info.pickle")
    if os.path.exists(usr_file_path) and os.path.isfile(usr_file_path):
        usr_file = open(usr_file_path, "rb")
        usrs_info = pickle.load(usr_file)
        usr_file.close()
    else:
        usr_file = open(usr_file_path, "wb")
        usrs_info = {'admin': 'admin'}
        pickle.dump(usrs_info, usr_file)
        usr_file.close()
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()


# 定义用户注册功能
def usr_sign_up():
    def sign_to_Website():
        # 以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        usr_file_path = os.path.join(os.getcwd(), "usrs_info.pickle")
        if os.path.exists(usr_file_path) and os.path.isfile(usr_file_path):
            usr_file = open(usr_file_path, "rb")
            exist_usr_info = pickle.load(usr_file)
            usr_file.close()
        else:
            exist_usr_info = {'admin': 'admin'}

        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            usr_file = open(usr_file_path, "wb")
            pickle.dump(exist_usr_info, usr_file)
            usr_file.close()
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然后销毁窗口。
            window_sign_up.destroy()

    # 定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set('example@python.com')  # 将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)

    # 下面的 sign_to_Website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Website)
    btn_comfirm_sign_up.place(x=180, y=120)


# login and sign up 按钮
btn_login = tk.Button(window, text="Login", command=usr_login)
btn_login.place(x=120, y=240)
btn_login = tk.Button(window, text="Sign up", command=usr_sign_up)
btn_login.place(x=200, y=240)

# 主窗口循环显示
window.mainloop()
