"""
@author: wanghongliang
@file: study_02_基础运算.py
@time: 2020/6/19 9:39 
"""

import numpy as np

npnum = np.arange(3, 15)

print(npnum)
print("npnum[0]: ", npnum[0])
print("npnum[3]: ", npnum[3])

npnum = np.arange(3, 15).reshape((3, 4))
print(npnum)
print("npnum[1]: ", npnum[1])
print("npnum[1][1]: ", npnum[1][1])
print("npnum[1, 1]: ", npnum[1, 1])
print("npnum[2, :]: ", npnum[2, :])  # 第二行所有的数
print("npnum[:, 1]: ", npnum[:, 1])  # 第一列的所有数
print("npnum[1, 1:3] : ", npnum[1, 1:3])  # 第二行所有的数

for row in npnum:
    print("row: ", row)

print("npnum.T: ", npnum.T)
for column in npnum.T:
    print("column: ", column)

# 三行四列变一行
print(npnum.flatten())

for item in npnum.flatten():
    print("item: ", item)

for item in npnum.flat:
    print("item: ", item)
