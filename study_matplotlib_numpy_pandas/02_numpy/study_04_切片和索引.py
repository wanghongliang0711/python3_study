"""
@author: blake.wang
@file: study_04_切片和索引.py
@time: 2021/11/9 17:27 
"""
import numpy as np

a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])  # [2 4 6]

# 也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作
a = np.arange(10)
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b) # [2 4 6]

a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5]
print(b)  # 5

a = np.arange(10)
print(a[2:])  # [2 3 4 5 6 7 8 9]

a = np.arange(10)
print(a[2:5])  # [2 3 4]

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[1:])  # [[3 4 5] [4 5 6]]

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a[...,1])   # 第2列元素  [2 4 5]
print (a[1,...])   # 第2行元素  [3 4 5]
print (a[1])   # 第2行元素  [3 4 5]
print (a[...,1:])  # 第2列及剩下的所有元素  [[2 3] [4 5] [5 6]]

# ========= NumPy 高级索引
"""
整数数组索引
以下实例获取数组中(0,0)，(1,1)和(2,0)位置处的元素。
"""
x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]]
print (y)  # [1 4 5]

# 获取了 4X3 数组中的四个角的元素
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
y = x[[[0,0],[3,3]],[[0,2],[0,2]]]  # 0,0  0,2     3,3  3,2
print  ('这个数组的四个角元素是：')
print (y)  # [[ 0  2] [ 9 11]]

a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b = a[1:3, 1:3]  # 行1:3  列1:3
c = a[1:3,[1,2]]  # 行1:3  列[1,2]
d = a[...,1:]   # 行所有...  列1:
print(b)  # [[5 6] [8 9]]
print(c)  # [[5 6] [8 9]]
print(d)  # [[2 3] [5 6] [8 9]]

"""布尔索引
布尔索引通过布尔运算（如：比较运算符）来获取符合指定条件的元素的数组。
"""
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
print  ('大于 5 的元素是：')
print (x[x >  5])  # [ 6  7  8  9 10 11]
# https://blog.csdn.net/zhangwin3/article/details/90575810
x = np.array([[  3,  8,  7],[  3,  9,  5],[  6,  7,  8],[  9,  10,  11]])
ss = x[..., -1] > 5
print(ss)
print(x[ss])
print(x[x[:, -1] > 5, 0:2])
print(x[x[:, -1] > 5, :])

# 使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan,  1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])  # [1. 2. 3. 4. 5.]
print (a[np.isnan(a)])  # [nan nan]

# 过滤掉非复数元素
a = np.array([1,  2+6j,  5,  3.5+5j])
print (a[np.iscomplex(a)])  # [2.+6.j 3.5+5.j]

"""花式索引
花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。对于使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应下标的行，如果目标是二维数组，那么就是对应位置的元素。
"""

x=np.arange(32).reshape((8,4))
print(x)
print (x[[4,2,1,7]])  # 取第4、2、1、7行的数据 [[16 17 18 19] [ 8  9 10 11] [ 4  5  6  7] [28 29 30 31]]
x=np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]]) # [[16 17 18 19] [24 25 26 27] [28 29 30 31] [ 4  5  6  7]]

# 传入多个索引数组
x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])  # [[ 4  7  5  6] [20 23 21 22] [28 31 29 30] [ 8 11  9 10]]
"""
[1,5,7,2],[0,3,1,2]
1,0  1,3  1,1  1,2
5,0  5,3  5,1  5,2
7,0  7,3  7,1  7,2
2,0  2,3  2,1  2,2
"""






