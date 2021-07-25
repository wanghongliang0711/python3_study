"""
@author: wanghongliang
@file: study_01_使用进程实现多任务.py
@time: 2021/7/22 13:45 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=14
# https://www.bilibili.com/video/BV1uw411d7sr?p=15
import threading
import time
import multiprocessing


def my_test01():
    while True:
        print("1-------------")
        time.sleep(1)


def my_test02():
    while True:
        print("2-------------")
        time.sleep(1)


def main():
    # 线程实现 方式
    # t1 = threading.Thread(target=my_test01)
    # t2 = threading.Thread(target=my_test02)
    # t1.start()
    # t2.start()

    # 进程实现 方式
    p1 = multiprocessing.Process(target=my_test01)
    p2 = multiprocessing.Process(target=my_test02)
    p1.start()
    p2.start()


"""
进程 能在 任务管理器中看到，如果在PyCharm中运行代码，
运行时会开到新增了3个进程

https://www.bilibili.com/video/BV1uw411d7sr?p=15
进程 运行时，相当于 子进程 共享主进程的代码，
进程比线程 浪费资源 可参考上面的链接

请看 study_04_进程池.py 有重要信息！！ 多进程 要在 main 函数中运行
"""


if __name__ == '__main__':
    main()
