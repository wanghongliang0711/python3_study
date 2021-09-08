#-*-coding:utf-8 -*-
import os
import openpyxl

path66 = os.getcwd()+'\\write.xlsx'
data = openpyxl.Workbook() 
sheet1 = data.active
sheet1.title = 'Statistical results'
sheet1['A1'] = 'good'

row = [1 ,2, 3, 4, 5]
row1 = [1 ,"", None, None, 5]
sheet1.append(row)
sheet1.append(row1)

sheet2 = data.create_sheet('Detailed results')
sheet2['A1'] = 'good333'
sheet2.append([1,2,3,None,4])  # None 插入数据也是 空的


data.save(path66)

# 以前从来没有 close 过，以后记得close
data.close()
