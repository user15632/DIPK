import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import joblib
import random
import pandas as pd

data = joblib.load('single_cell_ft.pkl')

dataframe = pd.DataFrame(data)
dataframe.to_csv('single_cell_ft.csv', index=False, sep=',')

df_dict = dict()
i = 0
for each in data:
    df_dict[i] = [each.split('_')[0]] + data[each]
    i += 1
dataframe = pd.DataFrame(df_dict)
dataframe.to_csv('single_cell_ft_.csv', index=False, sep=',')

"""
random.seed(0)
X = []
key = sorted(list(set([_.split('_')[0] for _ in list(data.keys())])))
Y = []
for each in data:
    Y.append(key.index(each.split('_')[0]))
    X.append(data[each])
X = np.array(X)
y = np.array(Y)
n_classes = 10

tsne = TSNE(init='pca', learning_rate='auto', n_components=2)
embedding = tsne.fit_transform(X)

# 绘制不同类别的散点图
plt.scatter(
    embedding[:, 0],
    embedding[:, 1],
    c=y,
    cmap='Spectral',
    s=5
)

cbar = plt.colorbar(boundaries=np.arange(n_classes+1)-0.5)
cbar.set_ticks(np.arange(n_classes).tolist())
cbar.set_ticklabels(key)
plt.show()
"""
