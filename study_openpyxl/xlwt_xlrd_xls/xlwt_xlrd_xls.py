#-*-coding:utf-8 -*-
'''
Created on 2019年5月15日

@author: 14668
'''
'''
# 如果对一个单元格重复操作，会引发
　　　returns error:
　　　    # Exception: Attempt to overwrite cell:
　　　　 # sheetname=u'sheet 1' rowx=0 colx=0
# 所以在打开时加cell_overwrite_ok=True 解决
　　  table = file.add_sheet('sheet name',cell_overwrite_ok=True )
'''
#######创建一个excel文件#######
#xls文件地址

import os

import xlrd
import xlwt

import  datetime as dt


xls_path = os.getcwd() + '\\demo_test.xls' 

#新建一个excel文件
xls = xlwt.Workbook()

dateFormat = xlwt.XFStyle()
dateFormat.num_format_str = 'yyyy/mm/dd'

#新建一个sheet
table = xls.add_sheet('my name is sheet',cell_overwrite_ok=True)

#写入数据,,从0行0列开始
table.write(0,0,99)  #数字类型
table.write(1,1,66660)
table.write(1,1,'hello') #文本类型
table.write(1,2,'hello') #文本类型
table.write(2,2,dt.date.today(),dateFormat) #日期列宽短有可能显示##

xls.save(xls_path)



#######读取一个Excel文件######
#打开Excel文件读取数据
data = xlrd.open_workbook(xls_path)


table = data.sheets()[0]          #通过索引顺序获取
# table = data.sheet_by_index(0) #通过索引顺序获取
#table = data.sheet_by_name(sheet_name)#通过名称获取


names = data.sheet_names()  #返回book中所有工作表的名字
print(names)

#行的操作
nrows = table.nrows  #获取该sheet中的有效行数
print(nrows)

#返回由该行中所有的单元格对象组成的列表  [empty:'', text:'hello', text:'hello']
print(table.row(1))

#返回由该列中所有的单元格对象组成的列表)[empty:'', text:'hello', text:'hello']
print(table.row_slice(1))  

#返回由该行中所有单元格的数据类型组成的列表 array('B', [0, 1, 1])
print(table.row_types(1, start_colx=0, end_colx=None))

#返回由该行中所有单元格的数据组成的列表['', 'hello', 'hello']
print(table.row_values(1, start_colx=0, end_colx=None))
#返回该列的有效单元格长度
print(table.row_len(0))




#列(colnum)的操作
ncols = table.ncols   #获取列表的有效列数
print(ncols)

##返回由该列中所有的单元格对象组成的列表[empty:'', text:'hello', empty:'']
print(table.col(1, start_rowx=0, end_rowx=None))

# #返回由该列中所有的单元格对象组成的列表[empty:'', text:'hello', empty:'']
print(table.col_slice(1, start_rowx=0, end_rowx=None))

##返回由该列中所有单元格的数据类型组成的列表[0, 1, 0]
print(table.col_types(1, start_rowx=0, end_rowx=None))

# #返回由该列中所有单元格的数据组成的列表['', 'hello', '']
print(table.col_values(1, start_rowx=0, end_rowx=None))




print(table.cell_value(1,1))  #返回单元格中的数据




