"""
@author: wanghongliang
@file: study_01_基本使用.py
@time: 2021/7/21 15:14 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=3
import threading
import time


def my_test1():
    for i in range(5):
        print("-----test1----%d-" % i)
        time.sleep(1)


def my_test2():
    for i in range(10):
        print("-----test2----%d-" % i)
        time.sleep(1)


def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=my_test1)
    print(threading.enumerate())
    t2 = threading.Thread(target=my_test2)

    t1.start()
    print(threading.enumerate())
    t2.start()

    while True:
        print(threading.enumerate())
        time.sleep(1)


"""
如果创建 Thread 时执行的函数运行结束，那么意味着这个子线程结束了。。。
主线程 运行到最后才会结束， 如果主线程意外挂了，子线程也会挂

子线程 从 t1.start() 时开始
当调用 Thread 的时候， 不会创建线程
当调用Thread 创建出来的实例对象的 start 方法的时候，
才会创建线程以及让这个线程开始运行
"""


if __name__ == '__main__':
    main()
