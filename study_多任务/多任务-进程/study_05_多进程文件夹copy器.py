"""
@author: wanghongliang
@file: study_05_多进程文件夹copy器.py
@time: 2021/7/23 11:27 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=20
import multiprocessing
import os
import random
import time


def make_dir(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except Exception as e:
        print("make_dir error . message: ", e)


def get_all_file(folder_path):
    try:
        result = []
        file_names = os.listdir(folder_path)
        for one_file in file_names:
            sub_dir = os.path.join(folder_path, one_file)
            if os.path.isfile(sub_dir):
                result.append(sub_dir)
        return result
    except Exception as e:
        print("get_all_file error . message: ", e)


# 复制文件
def copy_file(one_file, new_path):
    f_read = None
    f_write = None
    try:
        file_path, file_name = os.path.split(one_file)
        new_file_path = os.path.join(new_path, file_name)
        f_read = open(one_file, "rb")
        f_write = open(new_file_path, "wb")
        while True:
            sleep_time = random.random()
            print(os.getpid(), file_name, "---sleep_time--->, ", sleep_time)
            time.sleep(sleep_time)
            content = f_read.read(1024*10)  # 不写1024就一次读完，大文件容易崩
            if content:
                f_write.write(content)
            else:
                break
    except Exception as e:
        print("copy_file error . message: ", e)
    finally:
        if f_read is not None:
            print(os.getpid(), "---关闭 f_read---")
            f_read.close()
        if f_write is not None:
            print(os.getpid(), "---关闭 f_write---")
            f_write.close()


# ss = r"E:\kaifa\python37\Lib"
def main():
    # 1. 获取 文件夹路径
    folder_path = input("请输入文件夹路径： ")

    # 2. 获取 路径 下 所有的文件路径
    all_files = get_all_file(folder_path)

    # 3. 创建 新的文件夹
    new_path = os.path.join(os.getcwd(), "test[复件]")
    make_dir(new_path)

    # 4. 创建 进程池
    po = multiprocessing.Pool(2)

    # 5. 向进程池中添加 copy 文件的 任务
    for one_file in all_files:
        po.apply_async(copy_file, args=(one_file, new_path))

    po.close()
    po.join()


if __name__ == '__main__':
    main()
