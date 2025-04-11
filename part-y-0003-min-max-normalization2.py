import pandas as pd
from sklearn.preprocessing import MinMaxScaler

iris = pd.read_csv("./iris/iris.data", names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

x = iris.iloc[:, :4]

print(x.head(3))

y = iris.iloc[:, -1]

print(y.head(3))

"""
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
0                 5.1                3.5                 1.4                0.2
1                 4.9                3.0                 1.4                0.2
2                 4.7                3.2                 1.3                0.2

0    Iris-setosa
1    Iris-setosa
2    Iris-setosa

"""
