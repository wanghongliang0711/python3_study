"""
@author: wanghongliang
@file: study_02_基础运算.py
@time: 2020/6/19 9:39 
"""

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)   # [0 1 2 3]
print("a: ", a)
print("b: ", b)

c = a - b
print("a - b: ", c)
c = a + b
print("a + b: ", c)
c = a * b
print("a * b: ", c)
# c = a / b
# print("a / b: ", c)
c = a ** b  # 平方
print("a ** b: ", c)

# sin
c = 10*np.sin(a)
print("10*np.sin(a): ",c)

# 比较大小
print(b)  # [0 1 2 3]
print(b<3)  # [ True  True  True False]
print(b==3)  # [False False False  True]



#  二维数组
a = np.array([[1,2],[0,1]])
b = np.arange(1,5,1).reshape((2,2))

print(a)
print(b)

c = a*b
c_dot = np.dot(a,b)  # 矩阵相乘
# 另一种写法
c_dot_2 = a.dot(b)

print("c: ", c)
print("c_dot: ", c_dot)
print("c_dot_2: ", c_dot_2)


# 随机数
rando = np.random.random((2,3))  # 2 行 3列 从0~1的数字
print("rando: ", rando)

print("sum: ",np.sum(rando))
print("sum axis=1: ",np.sum(rando, axis=1))  # axis=1 行数求和
print("sum axis=0: ",np.sum(rando, axis=0))  # axis=0 列数求和

print("min: ",np.min(rando))
print("min axis=1: ",np.min(rando, axis=1))
print("max: ",np.max(rando))
print("max axis=0: ",np.max(rando, axis=0))

