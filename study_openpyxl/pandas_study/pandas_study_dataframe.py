#-*-coding:utf-8 -*-
'''
Created on 2019年6月3日

@author: wanghongliang
'''
from pandas import Series,DataFrame

#DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。它的竖行称之为 columns，横行跟前面的 Series 一样，称之为 index，也就是说可以通过 columns 和 index 来确定一个主句的位置。
data = {"name":['google','baidu','yahoo'],"marks":[100,200,300],"price":[1,2,3]}
f1 = DataFrame(data)
print(f1)
'''
这是定义一个 DataFrame 对象的常用方法——使用 dict 定义。字典的“键”（"name"，"marks"，"price"）就是 DataFrame 的 columns 的值（名称），字典中每个“键”的“值”是一个列表，它们就是那一竖列中的具体填充数据。上面的定义中没有确定索引，所以，按照惯例（Series 中已经形成的惯例）就是从 0 开始的整数。从上面的结果中很明显表示出来，这就是一个二维的数据结构（类似 excel 或者 mysql 中的查看效果）。
上面的数据显示中，columns 的顺序没有规定，就如同字典中键的顺序一样，但是在 DataFrame 中，columns 跟字典键相比，有一个明显不同，就是其顺序可以被规定，向下面这样做：
'''
f2 = DataFrame(data)#DataFrame(data,columns=['name','marks','marks'])
print(f2)
#跟 Series 类似的，DataFrame 数据的索引也能够自定义
f3 = DataFrame(data,columns=['name','marks','price'],index=['a','b','c'])
print(f3)

#定义 DataFrame 的方法，除了上面的之外，还可以使用“字典套字典”的方式。
newdata = {'lang':{'first':'python','second':'java'},'price':{'first':5000,'second':2000}}
f4 = DataFrame(newdata)
print(f4)
newdata = {"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000}} 
f4 = DataFrame(newdata) 
print(f4)
print(DataFrame(newdata, index=["firstline","secondline","thirdline"]) )

print(f4['lang'])#显示一列

#下面操作是给同一列赋值
newdata1 = {'username':{'first':'wangxing','second':'dadiao'},'age':{'first':24,'second':25}}
f6 = DataFrame(newdata1,columns=['username','age','sex'])
print(f6) 

f6['sex'] = 'man'
print(f6)

#也可以单独的赋值，除了能够统一赋值之外，还能够“点对点”添加数值，结合前面的 Series，既然 DataFrame 对象的每竖列都是一个 Series 对象，那么可以先定义一个 Series 对象，然后把它放到 DataFrame 对象中。如下：


ssex = Series(['男','女'],index=['first','second'])
f6['sex'] = ssex
print(f6)

#还可以更精准的修改数据吗？当然可以，完全仿照字典的操作
f7 = f6.loc[:,['username','age','sex']]
f7['age']['second'] = 30#有警告
print(f7)



