#-*-coding:utf-8 -*-
import os
import openpyxl

path66 = os.getcwd()+'\\write.xlsx'
data = openpyxl.Workbook() 
sheet1 = data.active
sheet1.title = 'Statistical results'
sheet1['A1'] = 'good'

sheet2 = data.create_sheet('Detailed results')
sheet2['A1'] = 'good333'



data.save(path66)
