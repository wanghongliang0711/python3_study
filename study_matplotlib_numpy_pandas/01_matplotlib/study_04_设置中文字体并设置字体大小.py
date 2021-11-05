"""
@author: blake.wang
@file: study_04_设置中文字体并设置字体大小.py
@time: 2021/11/3 19:01 
"""
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\SIMLI.TTF", size=12)

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(15, 8), dpi=80)

plt.plot(x,y)

# 调整x 轴的刻度
xtick_lables = ["10:{}".format(i) for i in range(60)]
xtick_lables += ["11:{}".format(i) for i in range(60)]

# plt.xticks(list(x)[::3], xtick_lables[::3],rotation=270)  # rotation 旋转的度数
plt.xticks(list(x)[::3], xtick_lables[::3],rotation=60)  # rotation 旋转的度数

yticks_lables = ["{}度".format(i) for i in range(15, 40, 2)]
plt.yticks(range(15, 40, 2), yticks_lables,rotation=60,fontproperties=my_font)

plt.show()
