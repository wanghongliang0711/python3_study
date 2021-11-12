"""
@author: blake.wang
@file: study_02_numpy数组的形状.py
@time: 2021/11/8 18:30 
"""
import numpy as np

t1 = np.arange(5)
print(t1)  # [0 1 2 3 4]
print(t1.shape)  # (5,)

t2 = np.array([[1,2,3],[4,5,6]])
print(t2)  # [[1 2 3] [4 5 6]]
print(t2.shape)  # (2, 3)  两行 三列

t3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(t3)  # [[[ 1  2  3] [ 4  5  6]] [[ 7  8  9] [10 11 12]]]
print(t3.shape)  # (2, 2, 3)  两块  两行 三列

# 修改 numpy形状
t4 = np.arange(8)
print(t4.reshape(2,4))  # [[0 1 2 3] [4 5 6 7]]

t5 = np.arange(24).reshape(2,3,4)
print(t5)  # [[[ 0  1  2  3] [ 4  5  6  7] [ 8  9 10 11]]  [[12 13 14 15] [16 17 18 19] [20 21 22 23]]]

print(t5.reshape(4,6))  # [[ 0  1  2  3  4  5] [ 6  7  8  9 10 11] [12 13 14 15 16 17] [18 19 20 21 22 23]]

# 变为一维
print(t5.reshape(24,))  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

# 当不知道数组大小时有两种办法变为一维
print(t5.reshape(t5.shape[0]*t5.shape[1]*t5.shape[2],))  # 这种方法需要知道数组是几维的
print(t5.flatten())  # 这种方法不需要知道结构

