"""
@author: wanghongliang
@file: study_03_通过队列完成进程间通信.py
@time: 2021/7/22 17:26 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=17
"""
其实 以前就 完成过 进程间 通信，利用的是socket，
不仅可以完成一台电脑间的通信，还能完成不同电脑间的通信
"""
import multiprocessing


def down_from_web(q):
    # 模拟从网上下载数据
    data = [11, 22, 33, 44]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)
    print("--下载器已经下载完了数据并且存入到队列中--")


def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break
    # 模拟数据处理
    print(waitting_analysis_data)


def main():
    # 1. 创建一个队列, 这个不能和 进程池一起用， multiprocessing.Manager().Queue()  multiprocessing.Manager().list 才能和进程池一起使用
    q = multiprocessing.Queue()  # 括号里面可以写大小，如果不写的就是根据电脑配置来，内存越大，存的越多

    # 2. 创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=down_from_web, args=(q, ))
    p2 = multiprocessing.Process(target=analysis_data, args=(q, ))

    p1.start()
    p2.start()

    """ 如果只是共享某一个数，参考： https://blog.csdn.net/zxyhhjs2017/article/details/92633309
    
    q1 = multiprocessing.Queue(3)
    q1.put("111")
    q1.put(333)
    q1.put([1, 2, "oo"])
    print("---1")
    # q.put(33)  # 如果满了，就会等待别人取走后才能继续运行
    print("---2")
    print(q1.get())  # 先放谁，就先取出谁，取不到后就会一直等待
    print(q1.get_nowait())  # q1.get() 不报错，q1.get_nowait() 取不到报错

    print(q1.full())  # 判断是否满了
    print(q1.empty())  # 判断是否为空
    """


if __name__ == '__main__':
    main()
