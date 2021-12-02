"""
@author: wanghongliang
@file: study_03_pandas_DataFrame索引.py
@time: 2021/11/28 16:31 
"""
import pandas as pd
import numpy as np


# pandas 取行或者列的注意点
# 方括号写数组，表示取行，对行进行操作
# 方括号写字符串，表示取列，对列进行操作
t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"), columns=list("wxyz"))
print(t1)
"""
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
print(t1[:2])
"""
   w  x  y  z
a  0  1  2  3
b  4  5  6  7
"""
print(t1[:2]["x"])
"""
a    1
b    5
Name: x, dtype: int32
"""
print(t1["y"])
"""
a     2
b     6
c    10
Name: y, dtype: int32
"""

print("*"*100)
# DataFrame.loc 通过标签索引行数据
t3 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"), columns=list("wxyz"))
print(t3)
"""
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
print(t3.loc["a", "z"])  # 3   a 行 z 列
print(type(t3.loc["a", "z"]))  # <class 'numpy.int32'>
# 取第 b 行
print(t3[1:2])
print(t3.loc["a"])
print(t3.loc["a", :])
"""
   w  x  y  z
b  4  5  6  7
w    0
x    1
y    2
z    3
Name: a, dtype: int32
w    0
x    1
y    2
z    3
Name: a, dtype: int32
"""
print("*"*100)
# 取第 y 列
print(t3["y"])
print(t3.loc[:,"y"])
"""
a     2
b     6
c    10
Name: y, dtype: int32
a     2
b     6
c    10
Name: y, dtype: int32
"""
print("*"*100)

# 取 多行 多列
print(t3.loc[["a","b"], ["w", "z"]])
"""
   w  z
a  0  3
b  4  7
"""
print(t3.loc["a":"c", ["w", "z"]])  # 注意 c 行被选中了
"""
   w   z
a  0   3
b  4   7
c  8  11
"""
print(t3.loc[["a","b"]])
"""
   w  x  y  z
a  0  1  2  3
b  4  5  6  7
"""
print(t3.loc[:, ["w", "z"]])
"""
   w   z
a  0   3
b  4   7
c  8  11
"""

print("*"*100)

# DataFrame.iloc 通过位置获取行数据
print(t3)
"""
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
print(t3.iloc[1])  # 取行
"""
w    4
x    5
y    6
z    7
Name: b, dtype: int32
"""

# 取列
print(t3.iloc[:, 1])
"""
a    1
b    5
c    9
Name: x, dtype: int32
"""

# 取多列
print(t3.iloc[:, [2,1]])
"""
    y  x
a   2  1
b   6  5
c  10  9
"""


# 取多行 多列
print(t3.iloc[[0,2], [2,1]])
"""
    y  x
a   2  1
c  10  9
"""
print(t3.iloc[1:,:2])
"""
   w  x
b  4  5
c  8  9
"""
t3.iloc[1:,:2] = 30
print(t3)
"""
    w   x   y   z
a   0   1   2   3
b  30  30   6   7
c  30  30  10  11
"""

# bool 索引
print("*"*100)
# 取第 y 列
print(t3)
"""
    w   x   y   z
a   0   1   2   3
b  30  30   6   7
c  30  30  10  11
"""
print(t3[t3["y"] > 3])
"""
    w   x   y   z
b  30  30   6   7
c  30  30  10  11
"""
print(t3[(t3["y"] > 3) & (t3["y"]<20)])
"""
    w   x   y   z
b  30  30   6   7
c  30  30  10  11
"""
print(t3[(t3["y"] > 3) |(t3["y"]<20)])
"""
    w   x   y   z
a   0   1   2   3
b  30  30   6   7
c  30  30  10  11
"""

# https://www.bilibili.com/video/BV1hx411d7jb?p=28&spm_id_from=pageDriver
# str
# 使用列表创建
data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'])
print(df)
"""
     Site  Age
0  Google   10
1  Runoob   12
2    Wiki   13
"""
print(df[df["Site"].str.len()>4])
"""
     Site  Age
0  Google   10
1  Runoob   12
"""
print(df["Site"].str.split("o"))
"""
0    [G, , gle]
1    [Run, , b]
2        [Wiki]
Name: Site, dtype: object
"""
print(df["Site"].str.split("o").tolist())
"""
[['G', '', 'gle'], ['Run', '', 'b'], ['Wiki']]
"""

