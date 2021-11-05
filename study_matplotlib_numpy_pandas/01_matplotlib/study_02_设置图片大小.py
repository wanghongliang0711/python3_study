"""
@author: blake.wang
@file: study_01_基础demo.py
@time: 2021/11/1 19:17 
"""
from matplotlib import pyplot as plt  # 绘图导入 pyplot 一般会重命名为plt

# 展示每隔两个小时的温度变化
x = range(2,26,2)  # [2,4,6,8 ... ,22,24]
y = [15,13,14.5,17,20,25,26,26,24,22,18,15]


"""
figure 指的是我们画的图
figsize 宽 高
dpi 没英寸多少个点，点多了，放大后不会模糊，有锯齿形
"""
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x,y)

# 设置x轴刻度
# plt.xticks(x)
xticks_lables = [i/2 for i in range(4, 49)]
# plt.xticks(xticks_lables)
plt.xticks(xticks_lables[::3])  # 太密集了，可以每三个取一个
# 设置y轴刻度
plt.yticks(range(min(y), max(y)+1))
# 设置刻度颜色，设置刻度倾斜等 参考 https://blog.csdn.net/Poul_henry/article/details/82590392

# 保存
# plt.savefig("./sig_size.png")
# plt.savefig("./sig_size.svg")  # 可以保存为svg矢量图格式，放大不会有锯齿

# 展示图形
plt.show()
