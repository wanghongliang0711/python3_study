"""
@author: wanghongliang
@file: study_04_进程池.py
@time: 2021/7/22 19:12 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=18
# https://www.bilibili.com/video/BV1uw411d7sr?p=19
"""
任务数不确定,一般用进程池, 否则任务数太多,服务器容易挂掉
进程池运行时, 主进程不会等待进程池运行结束,主进程运行结束后会直接挂掉

重要： 多进程 要在 main 函数中运行  if __name__ == '__main__':  可能旧版的python3不需要，因为视频中就没有放到main函数中
会打印出 四个 101，是因为 主进程 + 3个子进程 共打印出4个101？？？
101
----start----
101
101
101

"""
from multiprocessing import Pool
import os, time, random


test_num = 100
test_num += 1
print(test_num)

def worker(msg):
    t_start = time.time()
    print("%s 开始执行时间，进程号为%d" % (msg, os.getpid()))
    # random.random() 随机生成 0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(t_stop)
    print(type(t_stop))
    print(msg, " 执行完毕， 耗时%0.2f" % (t_stop-t_start))




def main():
    po = Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(0, 6):
        # Pool().apply_async(要调用的目标函数,(传递给目标的参数元组，))
        # 虽然加了 10个进程，但是一次只运行3个，其余的进程排队
        po.apply_async(worker, (i, ))

    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("====end=======")



if __name__ == '__main__':
    main()
