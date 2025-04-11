import pandas as pd
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

data = pd.read_csv("./iris/iris.data", names=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

X = data.iloc[:, : 4].values

#y = data.iloc[:, -1].values

scaler = StandardScaler()

X = scaler.fit_transform(X)

pca = PCA(n_components = 2)

pca_components = pca.fit_transform(X)

pca_data = pd.DataFrame(data = pca_components, columns = ["pca_1", "pca_2"])

y = pd.DataFrame(y, columns = ["class"])

final_df = pd.concat([pca_data, y], axis = 1)

print(final_df.head())

"""
      pca_1     pca_2        class
0 -2.264542  0.505704  Iris-setosa
1 -2.086426 -0.655405  Iris-setosa
2 -2.367950 -0.318477  Iris-setosa
3 -2.304197 -0.575368  Iris-setosa
4 -2.388777  0.674767  Iris-setosa

"""
