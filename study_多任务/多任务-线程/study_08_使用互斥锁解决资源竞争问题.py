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
    # 上锁，如果之前没有被上锁，那么此时，上锁成功
    # 如果上锁之前已经被上锁，那么此时会堵塞在这里，直到这个锁被解开为止
    mutex.acquire()
    for i in range(num):
        g_num += 1
    # 解锁
    mutex.release()
    print("---in test01 g_num = %d ---" % g_num)


def my_test02(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print("---in test02 g_num = %d ---" % g_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=my_test01, args=(1000000, ))
    t2 = threading.Thread(target=my_test02, args=(1000000, ))
    t1.start()
    t2.start()

    # 等待上面的 2个线程执行完毕
    time.sleep(2)

    print("---in main Thread g_num = %d---" % g_num)


""" print
---in test01 g_num = 1000000 ---
---in test02 g_num = 2000000 ---
---in main Thread g_num = 2000000---
"""


if __name__ == '__main__':
    main()
