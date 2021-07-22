"""
@author: wanghongliang
@file: study_05_多线程共享全局变量.py
@time: 2021/7/21 19:02 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=7
import threading
import time


def my_test01(temp):
    temp.append(33)
    print("-----in my_test01 temp = %s -----" % str(temp))


def my_test02(temp):
    print("-----in my_test02 temp= %s -----" % str(temp))


g_nums = [11, 22]


def main():
    # target 指定函数，一定不能加 （）
    # args 指定函数 的参数，是一个元组
    t1 = threading.Thread(target=my_test01, args=(g_nums, ))
    t2 = threading.Thread(target=my_test02, args=(g_nums, ))

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("------ in main Thread g_nums = %s---" % str(g_nums))


""" print
-----in my_test01 temp = [11, 22, 33] -----
-----in my_test02 temp= [11, 22, 33] -----
------ in main Thread g_nums = [11, 22, 33]---
"""


if __name__ == '__main__':
    main()
