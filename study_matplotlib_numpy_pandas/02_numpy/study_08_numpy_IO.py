"""
@author: blake.wang
@file: study_08_numpy_IO.py
@time: 2021/11/22 19:16 
"""
import numpy as np


"""https://www.runoob.com/numpy/numpy-io.html
numpy.save()
numpy.save(file, arr, allow_pickle=True, fix_imports=True)
"""

a = np.array([1, 2, 3, 4, 5])

# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)
# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('outfile2',a)

"""
可以看出文件是乱码的，因为它们是 Numpy 专用的二进制格式后的数据。
我们可以使用 load() 函数来读取数据就可以正常显示了：
"""
b = np.load('outfile.npy')
print(b)  # [1 2 3 4 5]

# np.savez
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
# c 使用了关键字参数 sin_array
np.savez("runoob.npz", a, b=b, sin_array = c)
r = np.load("runoob.npz")
print(r.files) # 查看各个数组名称
print(r["arr_0"]) # 数组 a
print(r["b"]) # 数组 b
print(r["sin_array"]) # 数组 c
"""
['b', 'sin_array', 'arr_0']
[[1 2 3]
 [4 5 6]]
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
[0.         0.09983342 0.19866933 0.29552021 0.38941834 0.47942554
 0.56464247 0.64421769 0.71735609 0.78332691]
"""

# savetxt  loadtxt
a = np.array([[1, 2, 3, 4, 5], [7, 8, 9, 10, 11]])
# delimiter 用什么分割数据
# fmt  保存的数据格式
# skiprows 跳过前几行。一般跳过表头
# dtype 指定数据类型
# usecols 取哪几列
# unpack 转置 效果 类似 numpy.transpose   ndarray.T
np.savetxt('out.txt', a, delimiter=",", fmt="%d,%d,%.3f,%.3f,%.3f")
b = np.loadtxt('out.txt', delimiter=",", skiprows=0, dtype=np.int32, usecols=(0,1,2))
b1 = np.loadtxt('out.txt', delimiter=",", skiprows=0, dtype=np.int32, usecols=(0,1,2), unpack=True)
print(b)
print("*"*20)
print(b1)
print("*"*20)
a = np.array([1, 2, 3, 4, 5])
np.savetxt('out1.txt', a, delimiter=",", fmt="%d")
b = np.loadtxt('out1.txt', delimiter=",")

print(b)
"""
[[1 2 3]
 [7 8 9]]
********************
[[1 7]
 [2 8]
 [3 9]]
********************
[1. 2. 3. 4. 5.]
"""
print("*"*60)
"""tofile fromfile
tofile()将数组中的数据以二进制格式写进文件
tofile()输出的数据不保存数组形状和元素类型等信息
fromfile()函数读回数据时需要用户指定元素类型，并对数组的形状进行适当的修改
"""
a = np.arange(12).reshape(4,3)
a.tofile("raw10.bin")
print(a.dtype)  # int32
print(a)

b = np.fromfile("raw10.bin",dtype=np.int64)  # 按照 np.int64 读入的数据是错误的
print(b)  #  [ 4294967296 12884901890 21474836484 30064771078 38654705672 47244640266]

b = np.fromfile("raw10.bin",dtype=np.int32)  # 按照 np.int32 读入的数据是一维的
print(b)  #  [ 0  1  2  3  4  5  6  7  8  9 10 11]
b.shape = 4,3
print(b)

print((a==b).all())  # True
"""
int32
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
[ 4294967296 12884901890 21474836484 30064771078 38654705672 47244640266]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
True
"""
