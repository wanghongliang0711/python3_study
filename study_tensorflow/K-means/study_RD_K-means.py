"""
@author: wanghongliang
@file: study_RD_K-means.py
@time: 2020/6/14 15:20 
"""
import time

import tensorflow as tf
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt


data = pd.read_csv("TAS-262_21C100446_120_0802_parse_sfc_analysis_7.csv")

print(data.head())

# 删除positioning_time和seq_no..列 删除列要加axis=1，默认是删除行的
data_x = data.drop(['positioning_time'], axis=1)

# print(data_x.head())

#  NaN  数据填充为 0
points = data_x.fillna(0)
# print(points)
cols = points.columns  # 返回表头
print(cols.tolist())

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(points)  # 归一化 数据变为0~1

df_normalized = pd.DataFrame(np_scaled, columns = cols)

# print(df_normalized)

# ？？？？？？？？？？？？
def input_fn():
  return tf.compat.v1.train.limit_epochs(
      tf.convert_to_tensor(df_normalized, dtype=tf.float32), num_epochs=1)


print("-----------------")
# print(input_fn())

print(data['Speed.speed'].values)
print(data['pulse'].values)

speed = data['Speed.speed'].values
pulse = data['pulse'].values
plt.scatter(speed, pulse, c='black', s=7)
plt.show()

print("-----------------")





# time.sleep(800)




num_clusters = 4  #  簇数
kmeans = tf.compat.v1.estimator.experimental.KMeans(
    num_clusters=num_clusters, use_mini_batch=False)

# train
num_iterations = 30  # 迭代次数
previous_centers = None
for _ in range(num_iterations):
  print("#####################################################################")
  kmeans.train(input_fn)
  cluster_centers = kmeans.cluster_centers()
  if previous_centers is not None:
    print('delta:', cluster_centers - previous_centers)
  previous_centers = cluster_centers
  print( 'score:', kmeans.score(input_fn))
print('cluster centers:', cluster_centers)

# # map the input points to their clusters
cluster_indices = list(kmeans.predict_cluster_index(input_fn))
print("cluster_indices:", cluster_indices)
# time.sleep(90)
for index, item in enumerate(cluster_indices):
  # print("item: ", item)
  cluster_index = cluster_indices[index]
  center = cluster_centers[cluster_index]
  print('point:', index, " item: ", item, ' is in cluster ', cluster_index, ' centered at ', center)



"""
当有多列数据时 数据如何在图中呈现？ x轴 和 y轴的值分别是什么 



相同的数据，有时集群中心不一致，这正常吗？  

"""





