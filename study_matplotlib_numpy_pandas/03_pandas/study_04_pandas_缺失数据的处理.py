"""
@author: blake.wang
@file: study_04_pandas_缺失数据的处理.py
@time: 2021/11/30 18:30 
"""
import pandas as pd
import numpy as np


t3 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"), columns=list("wxyz"))
print(t3)
"""
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
t3.iloc[1:,:2] = np.nan
print(t3)
"""
     w    x   y   z
a  0.0  1.0   2   3
b  NaN  NaN   6   7
c  NaN  NaN  10  11
"""
print(pd.isnull(t3))
"""
       w      x      y      z
a  False  False  False  False
b   True   True  False  False
c   True   True  False  False
"""
print(pd.notnull(t3))
"""
       w      x     y     z
a   True   True  True  True
b  False  False  True  True
c  False  False  True  True
"""
print(t3[pd.notnull(t3["w"])])
"""
     w    x  y  z
a  0.0  1.0  2  3
"""
# dropna 删除为nan 的 行或者 列 ;
# axis=0 删除行  axis=1 删除列
# how="all" 全为nan 的删除，  how="any" 有一个为nan的就删除
# inplace=True 就地修改，修改后直接会修改原数据，默认为 False，类似于 t3 = t3.dropna(axis=0, how="any")
print(t3.dropna(axis=0, how="all"))
"""
     w    x   y   z
a  0.0  1.0   2   3
b  NaN  NaN   6   7
c  NaN  NaN  10  11
"""
print(t3.dropna(axis=0, how="any"))
"""
     w    x  y  z
a  0.0  1.0  2  3
"""


# 为nan 填充数据
# fillna
print(t3)
"""
     w    x   y   z
a  0.0  1.0   2   3
b  NaN  NaN   6   7
c  NaN  NaN  10  11
"""
# 填充固定数字
print(t3.fillna(10))
"""
      w     x   y   z
a   0.0   1.0   2   3
b  10.0  10.0   6   7
c  10.0  10.0  10  11
"""
# 填充均值
print(t3.fillna(t3.mean()))
"""
     w    x   y   z
a  0.0  1.0   2   3
b  0.0  1.0   6   7
c  0.0  1.0  10  11
"""
# 只对某一列 填充均值
print(t3["x"].fillna(t3["x"].mean()))
"""
a    1.0
b    1.0
c    1.0
Name: x, dtype: float64
"""
t3["x"] = t3["x"].fillna(t3["x"].mean())
print(t3)
"""
     w    x   y   z
a  0.0  1.0   2   3
b  NaN  1.0   6   7
c  NaN  1.0  10  11
"""
"""
算均值时 pandas 不会把 nan 的算进去
但是 nunpy 会把nan 的算进去
"""
print(np.array([[1,6,5,np.nan],[1,6,5,np.nan]]).mean())  # nan
print(np.array([[1,1,1,1],[2,2,2,2]]).mean())  # 1.5




