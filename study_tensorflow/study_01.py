"""
@author: wanghongliang
@file: study_01.py
@time: 2020/5/22 20:48 
"""
import tensorflow as tf
import pandas as pd

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 用于忽略一个警告信息


print(tf.__version__)

data = pd.read_csv(r"D:\Study\python\python3_study\test.CSV")

print(data)

import matplotlib.pyplot as plt


plt.scatter(data.Education,data.Income)
# plt.show()  #  显示散点图

x = data.Education
y = data.Income

# 二元一次方程  f(X) = ax + b

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))
model.summary()
model.compile(optimizer='adam', loss="mse")  # loss损失函数方法 均方差


history = model.fit(x, y, epochs=5000)  # x y 训练1000次

# 预测 已知数据
print(model.predict(x))

# 预测新数据
print(model.predict(pd.Series(10)))
print(model.predict([[10],[20],[30],[40]]))

# hello = tf.constant("Hello World, TensorFlow!")
# # sess = tf.Session()
# print(hello)

# h = tf.constant("hell,TF")
# sess=tf.Session()
# print(sess.run(h))


