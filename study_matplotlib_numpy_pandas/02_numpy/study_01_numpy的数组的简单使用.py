"""
@author: wanghongliang
@file: study_01_numpy的数组的简单使用.py
@time: 2021/11/7 16:01 
"""
import random
import numpy as np

# 使用numpy 生成数组，得到ndarray 的数据类型
t1 = np.array([1,2,3])
print(t1)  # [1 2 3]
print(type(t1))  # <class 'numpy.ndarray'>

t2 = np.array(range(10))
print(t2)  # [0 1 2 3 4 5 6 7 8 9]
print(type(t2))  # <class 'numpy.ndarray'>

t3 = np.arange(10)
print(t3)  # [0 1 2 3 4 5 6 7 8 9]
print(type(t3))  # <class 'numpy.ndarray'>

t4 = np.arange(2, 10, 2)
print(t4)  # [2 4 6 8]
print(type(t4))  # <class 'numpy.ndarray'>


# 查看数据类型
print(t1.dtype)  # int32
print(t2.dtype)  # int32
print(t3.dtype)  # int32
print(t4.dtype)  # int32

# 创建numpy 时指定 数据类型
t5 = np.array(range(1,4),dtype="int8")
print(t5)  # [1 2 3]
print(t5.dtype)  # int8

t5 = np.array(range(1,4),dtype=float)
print(t5)  # [1. 2. 3.]
print(t5.dtype)  # float64

t5 = np.array(range(1,4),dtype=int)
print(t5)  # [1 2 3]
print(t5.dtype)  # int32

t5 = np.array([1,1,0,1,0],dtype=bool)
print(t5)  # [ True  True False  True False]
print(t5.dtype)  # bool  布尔类型

# 修改数据类型
t6 = t5.astype("int8")
print(t6)  # [1 1 0 1 0]
print(t6.dtype)  # int8

# numpy 中的小数
t7 = np.array([random.random() for i in range(3)])
print(t7)  # [0.94210459 0.37335804 0.38199125]
print(t7.dtype)  # float64

# 保留小数
t8 = np.round(t7,2)
print(t8)


