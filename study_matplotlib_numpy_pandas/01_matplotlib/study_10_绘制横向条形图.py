"""
@author: blake.wang
@file: study_09_绘制条形图.py
@time: 2021/11/5 14:41 
"""
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 展示排行前20的电影 名字和票房

# 票房
y = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]
# 电影
x = ["战狼{}".format(i) for i in range(len(y))]

# my_font= font_manager.FontProperties(fname=r"C:\Windows\Fonts\SIMLI.TTF", size=12)
my_font= font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=12)

# 设置图片大小
plt.figure(figsize=(15, 8), dpi=80)

# 生成横向的条形图 height 是条形图的宽度
plt.barh(range(len(x)),y,height=0.5)

plt.yticks(range(len(x)), x, fontproperties=my_font,rotation=45)

# 绘制网格
plt.grid(alpha=0.5)


plt.show()
