"""
@author: wanghongliang
@file: test01.py
@time: 2021/7/14 17:19 
"""
import time,sys
sys.path.append(r"D:\Study\python\python3_study\python3_study")
from Study_socket.Other.People_class import Tool



while True:
    tool1 = Tool()
    # print(Tool)
    tool1.set_result(tool1.get_result()+1)
    print(tool1.get_result())
    time.sleep(2)

