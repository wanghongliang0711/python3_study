"""
@author: wanghongliang
@file: study_01_基本使用.py
@time: 2021/7/21 15:14 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=1
import time
import threading


def sing():
    """唱歌 5秒"""
    for i in range(5):
        print("----- 正在唱 ： XXX -----")
        time.sleep(1)


def dance():
    """跳舞 5秒"""
    for i in range(5):
        print("----- 正在跳舞 -----")
        time.sleep(1)


def main():
    # 没有多任务
    # sing()
    # dance()

    # 使用多任务
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print("=== 主线程 继续向下运行 ====")
    """
    单核： 时间片轮转，假的多任务
    多核： 并行，真的多任务    CPU核数 大于等于 任务数 并行
           并发，假的多任务   任务数 大于 CPU核数 并发
    """


if __name__ == '__main__':
    main()
