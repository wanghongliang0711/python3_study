#-*-coding:utf-8 -*-
'''
Created on 2019年6月7日

@author: wanghongliang
'''
import csv
import pandas as pd
#普通方法读取CSV
'''
with open('120_1_D.csv') as f:
    for line in f:
        print(line)#,,,,,,,,,,,,,,,,,,,,,,,,,,0.0008,0.0028,0.0002,0,,

'''

# print(dir(csv))
# csv 的标准库
'''
csv_reader = csv.reader(open("120_1_D.csv"))
for row in csv_reader:
    print(row)#['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '-0.35', '0']
'''

#用 Pandas 读取
# marks = pd.read_csv('000_parse.csv')
# print(marks)

#方法一：默认读取第一个表单
# df=pd.read_excel('DisposeResult.xlsx')#这个会直接默认读取到这个Excel的第一个表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出


#方法二：通过指定表单名的方式来读取
# df=pd.read_excel('DisposeResult.xlsx',sheet_name='student')#可以通过sheet_name来指定读取的表单
# data=df.head()#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))#格式化输出


#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
# df=pd.read_excel('DisposeResult.xlsx',sheet_name=['python','student'])#可以通过表单名同时指定多个
df=pd.read_excel('DisposeResult.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
data=df.values#获取所有的数据，注意这里不能用head()方法哦~  没有读取表头
# print("获取到所有的值:\n{0}".format(data))#格式化输出


#读取指定的单行，数据会存在列表里面
data=df.ix[0].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
print("读取指定行的数据：\n{0}".format(data))

#读取指定的多行，数据会存在嵌套的列表里面：
data=df.ix[[1,2]].values#读取指定多行的话，就要在ix[]里面嵌套列表指定行数
print("读取指定行的数据：\n{0}".format(data))

#读取指定的行列：
data=df.ix[1,2]#读取第一行第二列的值，这里不需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))


#读取指定的多行多列值：
data=df.ix[[1,2],['title','data']].values#读取第一行第二行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))

#获取所有行的指定列
data=df.ix[:,['title','data']].values#读所有行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))


#获取行号并打印输出
print('*****************')
print("输出行号列表",df.index.values)

#获取列名并打印输出
print("输出列标题",df.columns.values)


#获取指定行数的值：
print("输出值",df.sample(0).values)#这个方法类似于head()方法以及df.values方法

#获取指定列的值：
print("输出值\n",df['data'].values)
lie = df['data'].values
print(lie[6])

#pandas处理Excel数据成为字典      处理成列表嵌套字典，且字典的key为表头名。
test_data=[]
for i in df.index.values:#获取行号的索引，并对其进行遍历：
    #根据i来获取每一行指定的数据 并利用to_dict转成字典
    row_data=df.ix[i,['case_id','title','data']].to_dict()
    test_data.append(row_data)
print("最终获取到的数据是：{0}".format(test_data))

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
df1.to_excel("output.xlsx")

df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
df1.to_excel("output1.xlsx",index=False)#





