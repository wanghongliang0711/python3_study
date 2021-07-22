"""
@author: wanghongliang
@file: study_07_多线程共享全局变量的问题-资源竞争.py.py
@time: 2021/7/21 19:33 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=8
import threading
import time


# 定义一个全局变量
g_num = 0


def my_test01(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("---in test01 g_num = %d ---" % g_num)


def my_test02(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("---in test02 g_num = %d ---" % g_num)


def main():
    t1 = threading.Thread(target=my_test01, args=(1000000, ))
    t2 = threading.Thread(target=my_test02, args=(1000000, ))
    t1.start()
    t2.start()

    # 等待上面的 2个线程执行完毕
    time.sleep(2)

    print("---in main Thread g_num = %d---" % g_num)


""" print 结果不是 2000000
---in test02 g_num = 1064773 ---
---in test01 g_num = 1181031 ---
---in main Thread g_num = 1181031---

g_num += 1  在真正执行时会被解析成很多步骤
比如：
    1. 获取 g_num 的值 0
    2. 把获取的值+1  0+1
    3. 把第2步的结果存储到g_num中
当同时执行 两个线程 时，
如果线程一执行到step2后停止，换线程二
线程二执行到step2后也停止，换线程一
线程一执行结束，值为 1，换线程二
线程二执行结束，值也为 1
此时g_num加了 两次 1 但是最终结果还是 1
就会导致出现 上面的情况，数值越大，越容易发生
https://www.bilibili.com/video/BV1uw411d7sr?p=8    10:00左右有讲解
"""


if __name__ == '__main__':
    main()
