"""
@author: blake.wang
@file: study_03_numpy数组创建的几种方法.py
@time: 2021/11/9 14:47 
"""
import numpy as np

"""
1、numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
"""
a = np.array([1,2,3])
print(a)  # [1 2 3]
a = np.array([[1,  2],  [3,  4]])
print(a)  # [[1 2] [3 4]]
a = np.array([1, 2, 3, 4, 5], ndmin =  2)
print(a)  # [[1 2 3 4 5]]
a = np.array([1,  2,  3], dtype = complex)
print (a)  # [1.+0.j 2.+0.j 3.+0.j]


""" numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
2、numpy.empty(shape, dtype = float, order = 'C')
shape	数组形状
dtype	数据类型，可选
order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
"""
x = np.empty((3,2), dtype = np.float64)
print(x)  # [[0 0] [0 0] [0 0]]  当为 int64 float64 时 会产生随机数，其他情况好像是产生 0


"""numpy.zeros 创建指定大小的数组，数组元素以 0 来填充：
3、numpy.zeros(shape, dtype = float, order = 'C')
shape	数组形状
dtype	数据类型，可选
order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
"""
# 默认为浮点数
x = np.zeros(5)  # [0. 0. 0. 0. 0.]
print(x)
# 设置类型为整数
y = np.zeros((5,), dtype = np.int64)
print(y)  # [0 0 0 0 0]

""" numpy.ones 创建指定形状的数组，数组元素以 1 来填充：
4、numpy.ones(shape, dtype = None, order = 'C')
shape	数组形状
dtype	数据类型，可选
order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
"""
# 默认为浮点数
x = np.ones(5)
print(x)  # [1. 1. 1. 1. 1.]
# 自定义类型
x = np.ones([2,2], dtype = np.int32)
print(x)  # [[1 1] [1 1]]


""" numpy.arange
5、numpy.arange(start, stop, step, dtype)
start	起始值，默认为0
stop	终止值（不包含）
step	步长，默认为1
dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
"""
x = np.arange(5)
print (x)  # [0 1 2 3 4]
# 设置了 dtype
x = np.arange(5, dtype =  float)
print (x)  # [0. 1. 2. 3. 4.]
# 设置了起始值、终止值及步长：
x = np.arange(10,20,2)
print (x)  # [10 12 14 16 18]


""" numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
6、np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
start	序列的起始值
stop	序列的终止值，如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
dtype	ndarray 的数据类型
"""
a = np.linspace(1,10,10)
print(a)  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# 设置元素全部是1的等差数列
a = np.linspace(1,1,10)
print(a)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# 将 endpoint 设为 false，不包含终止值：
a = np.linspace(10, 20,  5, endpoint =  False)
print(a)  # [10. 12. 14. 16. 18.]
# 设置间距 retstep 为 True
a = np.linspace(10, 19, 5, retstep=True)
print(a)  # (array([10.  , 12.25, 14.5 , 16.75, 19.  ]), 2.25)


""" numpy.logspace 函数用于创建一个于等比数列。格式如下：
7、np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
start	序列的起始值为：base ** start
stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
base	对数 log 的底数。
dtype	ndarray 的数据类型
"""
a = np.logspace(1.0, 2.0, num = 5)
print(a)  # [ 10.          17.7827941   31.6227766   56.23413252 100.        ]
a = np.logspace(0,9,10,base=2)
print(a)  # [  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]


""" numpy.full 返回一个根据指定shape和type,并用fill_value填充的新数组。
numpy.full(shape, fill_value, dtype=None, order='C')
shape：整数或整数序列
fill_value： 填充数组的值
dtype：数据类型，可选
"""
a = np.full((2,3), 6)
print(a)  # [[6 6 6] [6 6 6]]

a = np.full((2,3,3), 6)
print(a)
print(a.size)
