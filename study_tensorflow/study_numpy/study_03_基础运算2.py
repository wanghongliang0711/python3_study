"""
@author: wanghongliang
@file: study_02_基础运算.py
@time: 2020/6/19 9:39 
"""

import numpy as np

# rando = np.random.random((3,4))
rando = np.arange(2, 14).reshape((3, 4))
print("rando: ", rando)

print("最小值位置: ", np.argmin(rando))  # 最小值位置 7
print("最大值位置: ", np.argmax(rando))  # 最大值位置 3
# 平均值
print("平均值 : ", np.mean(rando))
print("平均值 行: ", np.mean(rando, axis=1))
print("平均值 列: ", np.mean(rando, axis=0))
print("平均值 : ", rando.mean())
print("平均值 : ", np.average(rando))

print("中位数 ：", np.median(rando))
print("累加值 ：", np.cumsum(rando))
print("累差值 ：", np.diff(rando))

rando = np.arange(14, 2, -1).reshape((3, 4))
print(rando)
print("排序，逐行排序 ： ", np.sort(rando))

print(np.clip(rando, 5, 10))  # 大于10的变成10  小于5的变成5



