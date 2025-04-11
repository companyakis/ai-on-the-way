import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("./iris/iris.data", names=["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

print(data.head())

X = data.iloc[:, : 4].values

print(X[:3])

y = data.iloc[:, -1].values

scaler = StandardScaler()

X = scaler.fit_transform(X)

print(X[:3])

"""
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm        class
0                 5.1                3.5                 1.4                0.2  Iris-setosa
1                 4.9                3.0                 1.4                0.2  Iris-setosa
2                 4.7                3.2                 1.3                0.2  Iris-setosa
3                 4.6                3.1                 1.5                0.2  Iris-setosa
4                 5.0                3.6                 1.4                0.2  Iris-setosa

[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]]
 
[[-0.90068117  1.03205722 -1.3412724  -1.31297673] 
 [-1.14301691 -0.1249576  -1.3412724  -1.31297673] 
 [-1.38535265  0.33784833 -1.39813811 -1.31297673]]

"""
