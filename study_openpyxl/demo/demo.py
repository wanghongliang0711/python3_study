#-*-coding:utf-8 -*-
'''
Created on 2019年4月28日

@author: 14668
'''
import os

import xlwt

path1 = os.getcwd()+'\\demo.xls'
# print(path1)

xls = xlwt.Workbook()
style = xlwt.XFStyle() # 初始化样式
sht1 = xls.add_sheet('first')
sht2 = xls.add_sheet('second')

#添加字段，第一行
sht1.write(0,0,2)
sht1.write(0,1,2)
sht1.write(0,2,11)
sht1.write(0,3,88)
sht1.write(0,4,66.00300)

#数据，第二行
sht1.write(1,0,0.3300)
sht1.write(1,1,'11')
sht1.write(1,2,'wang')
sht1.write(1,3,'13')
sht1.write(1,4,'14')

#数据，第三行
sht1.write(2,0,'20')
sht1.write(2,1,'21')
sht1.write(2,2,'22')
sht1.write(2,3,'23')
sht1.write(2,4,'24')


xls.save(path1)






