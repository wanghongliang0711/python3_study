"""
@author: blake.wang
@file: study_09_绘制条形图.py
@time: 2021/11/5 14:41 
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 展示五部电影三天的票房

a = ["猩球崛起3:终极之战","郭刻尔克","蜘蛛侠:英雄归来","战狼2"]

b_14 = [2358,399,2358,362]
b_15 = [12357,156,2045,168]
b_16 = [15746,312,4497,319]

# my_font= font_manager.FontProperties(fname=r"C:\Windows\Fonts\SIMLI.TTF", size=12)
my_font= font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=12)

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

# 设置图形大小
plt.figure(figsize=(13,7), dpi=80)

plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

# 设置图例
plt.legend(prop=my_font)

# 设置x轴刻度
plt.xticks(x_15,a,fontproperties=my_font)

plt.show()
