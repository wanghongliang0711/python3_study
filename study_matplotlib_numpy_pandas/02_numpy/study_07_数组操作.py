"""
@author: wanghongliang
@file: study_07_数组操作.py
@time: 2021/11/21 16:08 
"""
import numpy as np

a = np.arange(8)
print('原始数组 ： ')
print(a)  # [0 1 2 3 4 5 6 7]
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)
"""
原始数组 ： 
[0 1 2 3 4 5 6 7]
修改后的数组：
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
"""

# numpy.ndarray.flat 是一个数组元素迭代器，实例如下:
a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)
# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element, end=", ")
"""
原始数组：
[0 1 2]
[3 4 5]
[6 7 8]
迭代后的数组：
0, 1, 2, 3, 4, 5, 6, 7, 8, 
"""
print('\n')

# numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
a = np.arange(8).reshape(2, 4)
print('原数组：')
print(a)
print('\n')
# 默认按行
print('展开的数组：')
print(a.flatten())
print('\n')
print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))
"""
原数组：
[[0 1 2 3]
 [4 5 6 7]]
展开的数组：
[0 1 2 3 4 5 6 7]
以 F 风格顺序展开的数组：
[0 4 1 5 2 6 3 7]
"""
print('\n')
print("============================")
# numpy.ravel() 展平的数组元素，顺序通常是"C风格"
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
x = a.ravel()
print(x)
print('\n')
x[1] = 100
print(x)
print(a)

""" 发现一个问题a.ravel(order='F') 时修改数据不会影响原始数据
原数组：
[[0 1 2 3]
 [4 5 6 7]]

调用 ravel 函数之后：
[0 1 2 3 4 5 6 7]

[  0 100   2   3   4   5   6   7]
[[  0 100   2   3]
 [  4   5   6   7]]
"""
# print('以 F 风格顺序调用 ravel 函数之后：')
# b = a.ravel(order='F')
# print(b)
# b[1] = 100
# print(b)
# print(a)

##  翻转数组



