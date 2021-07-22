"""
@author: wanghongliang
@file: study_04_通过继承Thread类创建线程.py
@time: 2021/7/21 18:40 
"""
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)  # name 属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    t.start()
"""
https://www.bilibili.com/video/BV1uw411d7sr?p=4
https://www.bilibili.com/video/BV1uw411d7sr?p=5
新创建的类 必须 继承 threading.Thread
新创建的类 必须 写 run 方法
t.start() 会自动调用 自己写的 run 方法
"""
