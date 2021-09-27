"""
@author: wanghongliang
@file: study_02_创建一个可迭代对象.py
@time: 2021/7/25 16:09 
"""
# https://www.bilibili.com/video/BV1uw411d7sr?p=21
from collections.abc import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        pass


classmate = Classmate()

classmate.add("one")
classmate.add("two")
classmate.add("three")

print("判断classmate是否是可以迭代的对象: ", isinstance(classmate, Iterable))

for temp in classmate:
    print(temp)
# TypeError: iter() returned non-iterator of type 'NoneType'
