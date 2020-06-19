"""
@author: wanghongliang
@file: study_01.py
@time: 2020/6/18 19:19 
"""
import numpy as np
array = np.array([[1,2,3],[4,5,6]])

print(array)  # 打印出矩阵
print("几维数组： ",array.ndim)
print("行数，列数 ： ",array.shape)
print("大小 ：", array.size)
print("数据类型 ：", array.dtype)


a1 = np.array([2,3,4],dtype=np.float32)
a2 = np.array([2,3,4],dtype=np.int64)
a3 = np.array([2,3,4],dtype=np.float16)
print(a1.dtype)
print(a1)
print(a2.dtype)
print(a2)
print(a3.dtype)
print(a3)

# 定义全部为 0 的矩阵
zero1 = np.zeros( (3,4))
print("zero1 类型 ", zero1.dtype)
print(zero1)
# 定义全部为 1 的矩阵
ones1 = np.ones( (3,4))
print("ones 类型 ", ones1.dtype)
print(ones1)
# 定义全部为 根据类型随机产生数据 的矩阵  empty
empty1 = np.empty( (3,4) , dtype=np.float32)
print("empty 类型 ", empty1.dtype)
print(empty1)
#   https://www.bilibili.com/video/BV1Ex411L7oT?p=4

range = np.arange(3,10, 2)  # 3 到10之间  步长是2
print("range : ",range.dtype)
print(range)
range1 = np.arange(15).reshape((3,5))
print(range1)
# 生产线段
range2 = np.linspace(1, 10, 5)  # 1到10  5段
print(range2)
range3 = np.linspace(1, 10, 6).reshape((2,3))  # 1到10
print(range3)













