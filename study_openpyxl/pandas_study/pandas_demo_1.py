#-*-coding:utf-8 -*-
'''
Created on 2019年6月10日

@author: wanghongliang
'''
import pandas as pd

#读取csv所有内容
marks = pd.read_csv('120_1_D.csv',low_memory = False)
#根据列名取得想要的列
pf = marks[['Metadata.seq_no','Metadata.Sensor.Gps.positioning_time']]
#去掉全部为空的行
#df.dropna(axis=0, how='any', inplace=True)
# axis：0-行操作（默认），1-列操作 
# how：any-只要有空值就删除（默认），all-全部为空值才删除 
# inplace：False-返回新的数据集（默认），True-在愿数据集上操作
pf=pf.dropna(how = 'all')
#重命名表头
'''方法一：暴力方法
a.columns = ['a','b','c']
但是缺点是必须写三个，要不报错。

方法二：较好的方法
a.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace = True)
好处是可以随意改个数：
a.rename(columns={'A':'a', 'C':'c'}, inplace = True)
'''
pf.rename(columns={'Metadata.seq_no':'seq_no', 'Metadata.Sensor.Gps.positioning_time':'positioning_time'}  ,inplace = True)

pf.to_excel("output2.xlsx",index=False)#





















