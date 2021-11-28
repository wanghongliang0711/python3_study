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


