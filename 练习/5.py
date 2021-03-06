import numpy as np
import pandas as pd
from sklearn import datasets
from scipy.io import loadmat
from sklearn.cluster import dbscan
import matplotlib.pyplot as plt

# 导入数据库中的make_moons，加入高斯噪声，_ 表示后续不使用的临时变量
# X, _ = datasets.make_moons(500, noise=0.1, random_state=1)
file = 'W:\Study Flies\MATLAB\Data\MyData1.mat'
data1 = loadmat(file, mat_dtype=True)
X = data1['DisMat']
# print(X)
# 把数据放入到DataFrame数据结构中，命名行列
df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])
# 设置图中的文本与散点大小和透明度
df.plot.scatter('Feature1', 'Feature2', title='dataset by make_moon', s=6, alpha=0.6)

# 开始聚类分析，eps为邻域半径，min_samples为点阈值，core_samples是核心点索引，cluster_ids中值为-1的点代表噪声点
core_samples, cluster_ids = dbscan(X, eps=5, min_samples=12)

# np.c_[X, cluster_ids]吧X与cluster_ids切片前后对应堆叠成2维数据
df = pd.DataFrame(np.c_[X, cluster_ids], columns=['Feature1', 'Feature2', 'cluster_id'])
# 把cluster_id列的数据格式改为i2
df['cluster_id'] = df['cluster_id'].astype('i2')
df.plot.scatter('Feature1', 'Feature2', title='DBSCAN cluster result', s=6, alpha=0.6,
                c=list(df['cluster_id']), cmap='rainbow', colorbar=True,
                )

# 可视化
plt.show()
