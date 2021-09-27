"""
@author: wanghongliang
@file: study_01_迭代器_判断是否可以迭代.py
@time: 2021/7/25 15:49 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=21
from collections.abc import Iterable


# 判断是否可迭代
print(isinstance([11,2,3], Iterable))  # True
print(isinstance((11,2,3), Iterable))  # True
print(isinstance("str", Iterable))  # True
print(isinstance(100, Iterable))  # False




