"""
@author: wanghongliang
@file: study_01_基本使用.py
@time: 2021/7/21 15:14 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=3
import threading
import time


def test1():
    for i in range(5):
        print("-----test1----%d-" % i)


def test2():
    for i in range(5):
        print("-----test2----%d-" % i)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print(threading.enumerate())
    """
    print(threading.enumerate()) 的打印结果不固定，有可能是3或2个 有可能只有一个
    [<_MainThread(MainThread, started 5944)>, <Thread(Thread-1, started 6924)>, <Thread(Thread-2, started 5064)>]
    
    如果加了time.sleep 等两个子线程运行结束，最后打印就会只有一个主线程
    [<_MainThread(MainThread, started 6728)>]
    
    
    """


if __name__ == '__main__':
    main()
