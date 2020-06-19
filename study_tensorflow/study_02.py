"""
@author: wanghongliang
@file: study_01.py
@time: 2020/5/22 20:48 
"""
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 用于忽略一个警告信息


print(tf.__version__)

data = pd.read_csv(r"D:\Study\python\python3_study\study2.CSV")
# 电视投放量  广播投放量  报纸投放量  销量（预测值）

print(data)



a = tf.constant(2.)
b = tf.constant(4.)

print("a+b=",a+b)





