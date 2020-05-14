"""
@author: wanghongliang
@file: 柱状图-Bar.py
@time: 2020/5/14 15:53 
"""

from pyecharts.charts import Bar
from pyecharts import options as opts

# //设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# //设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

bar = Bar()
bar.add_xaxis(columns)
bar.add_yaxis("商家A", data1)
bar.add_yaxis("商家B", data2)
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题1", subtitle="副标题1"))
bar.render()

