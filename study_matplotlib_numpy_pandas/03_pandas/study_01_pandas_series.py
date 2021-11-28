"""
@author: wanghongliang
@file: study_01_pandas_series.py
@time: 2021/11/28 10:48 
"""
import pandas as pd
import numpy as np

t = pd.Series([4,5,6])
print(t)
print(type(t))  # <class 'pandas.core.series.Series'>
print(t[1])  # 5
"""
0    4
1    5
2    6
dtype: int64
<class 'pandas.core.series.Series'>
5
"""
print("*"*10)
# 指定索引
t2 = pd.Series([2,4,6,8], index=list("abcd"))
print(t2)
print(t2["c"])  # 6
print(t2.astype(float))
print(t2[t2>5])
"""
a    2
b    4
c    6
d    8
dtype: int64
6
a    2.0
b    4.0
c    6.0
d    8.0
dtype: float64
c    6
d    8
dtype: int64
"""
print("*"*10)
# 通过字典创建 Series
temp_dict = {"name": "wang1", "age": 18, "tel": 10010}

t3 = pd.Series(temp_dict)
print(t3)
print(t3["age"])  # 18
print(t3[1])  # 18
print(t3[:2])
print(t3[[1,2]])
print(t3[["name","tel"]])
"""
name    wang1
age        18
tel     10010
dtype: object
18
18
name    wang1
age        18
dtype: object
age       18
tel    10010
dtype: object
name    wang1
tel     10010
dtype: object
"""
print(t3.index)  # Index(['name', 'age', 'tel'], dtype='object')
print(type(t3.index))  # <class 'pandas.core.indexes.base.Index'>

print(t3.values)  # ['wang1' 18 10010]
print(type(t3.values))  # <class 'numpy.ndarray'>





