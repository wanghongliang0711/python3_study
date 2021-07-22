"""
@author: wanghongliang
@file: study_05_多线程共享全局变量.py
@time: 2021/7/21 19:02 
"""
import threading
import time


g_num = 100


def my_test01():
    global g_num
    g_num += 1
    print("-----in my_test01 g_num= %d -----" % g_num)


def my_test02():
    print("-----in my_test02 g_num= %d -----" % g_num)


def main():
    t1 = threading.Thread(target=my_test01)
    t2 = threading.Thread(target=my_test02)

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("------ in main Thread g_num= %d---" % g_num)


""" print
-----in my_test01 g_num= 101 -----
-----in my_test02 g_num= 101 -----
------ in main Thread g_num= 101---
"""


if __name__ == '__main__':
    main()
