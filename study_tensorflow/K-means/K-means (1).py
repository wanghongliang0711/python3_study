import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn import preprocessing

filePath = './data/TAS-262_21C100446_120_0802_parse_sfc_analysis_7.csv'
data = pd.read_csv(filePath)
print(data.head())
data_x = data.drop(['positioning_time','seq_no'], axis=1)
print(data_x.head())

points = data_x.fillna(0)
cols = points.columns

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(points)
df_normalized = pd.DataFrame(np_scaled, columns = cols)

print(df_normalized)

def input_fn():
  return tf.compat.v1.train.limit_epochs(
      tf.convert_to_tensor(df_normalized, dtype=tf.float32), num_epochs=1)

num_clusters = 4
kmeans = tf.compat.v1.estimator.experimental.KMeans(
    num_clusters=num_clusters, use_mini_batch=False)

# train
num_iterations = 30
previous_centers = None
for _ in range(num_iterations):
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
for index, item in enumerate(cluster_indices):
  cluster_index = cluster_indices[item]
  center = cluster_centers[cluster_index]
  print('point:', index, 'is in cluster', cluster_index, 'centered at', center)

