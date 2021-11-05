"""
@author: blake.wang
@file: study_03_xy轴旋转显示字符串.py
@time: 2021/11/3 18:32 
"""
from matplotlib import pyplot as plt
import random


x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(15, 8), dpi=80)

plt.plot(x,y)

# 调整x 轴的刻度
xtick_lables = ["10:{}".format(i) for i in range(60)]
xtick_lables += ["11:{}".format(i) for i in range(60)]

# plt.xticks(list(x)[::3], xtick_lables[::3],rotation=270)  # rotation 旋转的度数
plt.xticks(list(x)[::3], xtick_lables[::3],rotation=60)  # rotation 旋转的度数

yticks_lables = ["{}tem".format(i) for i in range(15, 40, 2)]
plt.yticks(range(15, 40, 2), yticks_lables,rotation=60)

plt.show()


