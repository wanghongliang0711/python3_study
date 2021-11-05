"""
@author: blake.wang
@file: study_01_基础demo.py
@time: 2021/11/1 19:17 
"""
from matplotlib import pyplot as plt  # 绘图导入 pyplot 一般会重命名为plt


# 展示每隔两个小时的温度变化
x = range(2,26,2)  # [2,4,6,8 ... ,22,24]
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]

plt.plot(x,y)
plt.show()
