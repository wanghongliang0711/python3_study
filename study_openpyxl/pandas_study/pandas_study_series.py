#-*-coding:utf-8 -*-
'''
Created on 2019年6月3日

@author: wanghongliang
'''
from pandas import Series
import pandas as pd

#Series 就如同列表一样，一系列数据，每个数据对应一个索引值。
#Series 就是“竖起来”的 list：
s = Series([1,4,'ww','t'])
print(s)
print(type(s))#<class 'pandas.core.series.Series'>

print(s.index)#RangeIndex(start=0, stop=4, step=1)
print(s.values)#[1 4 'ww' 't']
print(type(s.values))#<class 'numpy.ndarray'>
li = s.values
print(li[2])
print(type(li))#<class 'numpy.ndarray'>

#列表的索引只能是从 0 开始的整数，Series 数据类型在默认情况下，其索引也是如此。不过，区别于列表的是，Series 可以自定义索引：
s2 = Series(['wangxing','man',24],index=['name','sex','age'])
print(s2)
print(s2['name'])
s2['name'] = 'wanghonglaing'
print(s2)

#读者是否注意到，前面定义 Series 对象的时候，用的是列表，即 Series() 方法的参数中，第一个列表就是其数据值，如果需要定义 index，放在后面，依然是一个列表。除了这种方法之外，还可以用下面的方法定义 Series 对象：
sd = {'python':9000,'c++':9001,'c#':9000}
s3 = Series(sd)
print(s3)
#现在是否理解为什么前面那个类似 dict 了？因为本来就是可以这样定义的。
#这时候，索引依然可以自定义。Pandas 的优势在这里体现出来，如果自定义了索引，自定的索引会自动寻找原来的索引，如果一样的，就取原来索引对应的值，这个可以简称为“自动对齐”。
s4 = Series(sd,index=['java','c++','c#'])
print(s4)
#在 Pandas 中，如果没有值，都对其赋给 NaN。
#Pandas 有专门的方法来判断值是否为空。
print(pd.isnull(s4))

#此外，Series 对象也有同样的方法：
print(s4.isnull())

#其实，对索引的名字，是可以从新定义的：
s4.index = ['语文','数学','English']
print(s4)

#对于 Series 数据，也可以做类似下面的运算（关于运算，后面还要详细介绍）：
print(s4*2)

print(s4[s4>9000])
















