"""
@author: wanghongliang
@file: study_02_pandas_DataFrame.py
@time: 2021/11/28 14:04 
"""
import pandas as pd
import numpy as np


t = pd.DataFrame(np.arange(12).reshape(3,4))
print(t)
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""

# index、columns 使用：
t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"), columns=list("wxyz"))
print(t1)
"""
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""

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

# 使用字典创建
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)
"""
     Site  Age
0  Google   10
1  Runoob   12
2    Wiki   13
"""
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)
"""
   a   b     c
0  1   2   NaN
1  5  10  20.0
"""
print("*"*30)
# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[1])
print("*"*30)
print(df.loc[[0, 1]])
print("*"*30)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])
"""
 a   b     c
0  1   2   NaN
1  5  10  20.0
a    1.0
b    2.0
c    NaN
Name: 0, dtype: float64
a     5.0
b    10.0
c    20.0
Name: 1, dtype: float64
******************************
   a   b     c
0  1   2   NaN
1  5  10  20.0
******************************
calories    380
duration     40
Name: day2, dtype: int64
"""
print("*"*90)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
"""
   a   b     c
0  1   2   NaN
1  5  10  20.0
"""
print(df.index)  # RangeIndex(start=0, stop=2, step=1)
print(df.columns)  # Index(['a', 'b', 'c'], dtype='object')
print(df.values)  # [[ 1.  2. nan] [ 5. 10. 20.]]
print(df.shape)  # (2, 3)
print(df.ndim)  # 数据维度 2
print(df.dtypes)  # 列数据类型
"""
a      int64
b      int64
c    float64
dtype: object
"""
print("*"*80)
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   a       2 non-null      int64  
 1   b       2 non-null      int64  
 2   c       1 non-null      float64
dtypes: float64(1), int64(2)
memory usage: 176.0 bytes
None
"""
print(df.describe())
"""
              a          b     c
count  2.000000   2.000000   1.0
mean   3.000000   6.000000  20.0
std    2.828427   5.656854   NaN
min    1.000000   2.000000  20.0
25%    2.000000   4.000000  20.0
50%    3.000000   6.000000  20.0
75%    4.000000   8.000000  20.0
max    5.000000  10.000000  20.0
"""

print("*"*90)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
"""
   a   b     c
0  1   2   NaN
1  5  10  20.0
"""
# ascending=True 升序
# ascending=False 降序
df = df.sort_values("c", ascending=False)
print(df)
"""
   a   b     c
1  5  10  20.0
0  1   2   NaN
"""




