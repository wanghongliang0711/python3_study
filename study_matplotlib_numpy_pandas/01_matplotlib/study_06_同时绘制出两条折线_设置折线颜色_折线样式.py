"""
@author: blake.wang
@file: study_06_同时绘制出两条折线_设置折线颜色_折线样式.py
@time: 2021/11/4 16:35 
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager


"""
a 是自己  b 是同桌
x 轴是年龄  y 轴是女朋友的数量
"""
a = [1,0,2,1,5,2,3,6,9,5,1,2,3,1,2,3,2,1,2,1]
b = [1,3,1,1,2,1,1,1,4,4,4,2,2,2,4,1,1,4,1,2]

x = range(11, 31)

my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\SIMLI.TTF", size=12)

# 设置图形大小
plt.figure(figsize=(15, 8), dpi=80)

# plot 增加 label 和 plt.legend() 可以显示tuli
# plot 增加 color 可以修改 线条颜色
# linestyle  线条风格  linestyle 也适用于绘制网格
# - 实线  -- 虚线  -. 点划线  : 点虚线  "" 留空或者空格无线条
# linewidth  线条粗细
# alpha  透明度
plt.plot(x, a, label="自己", color="orange", linestyle="--", linewidth=3, alpha=0.3)
plt.plot(x, b, label="同桌", color="#FF69B4", linestyle="-.",linewidth=6, alpha=0.6)

# 设置x刻度
xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, xtick_labels, fontproperties=my_font)
plt.yticks(range(0,11))

# 绘制网格 linestyle 也适用于绘制网格
plt.grid(alpha=0.6, linestyle="--")

# 添加图例  prop 显示中文，只有这里是 prop其他地方都是 fontproperties
# loc="upper left" 参数可以修改 图例位置 默认是右上
plt.legend(prop=my_font,loc="upper left")

plt.show()
