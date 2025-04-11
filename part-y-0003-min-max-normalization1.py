import pandas as pd
from sklearn.preprocessing import MinMaxScaler

iris = pd.read_csv("./iris/iris.data", names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

print(iris.head())

print(iris.describe())

"""
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm        class
0                 5.1                3.5                 1.4                0.2  Iris-setosa
1                 4.9                3.0                 1.4                0.2  Iris-setosa
2                 4.7                3.2                 1.3                0.2  Iris-setosa
3                 4.6                3.1                 1.5                0.2  Iris-setosa
4                 5.0                3.6                 1.4                0.2  Iris-setosa

       sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
count          150.000000         150.000000          150.000000         150.000000
mean             5.843333           3.054000            3.758667           1.198667
std              0.828066           0.433594            1.764420           0.763161
min              4.300000           2.000000            1.000000           0.100000
25%              5.100000           2.800000            1.600000           0.300000
50%              5.800000           3.000000            4.350000           1.300000
75%              6.400000           3.300000            5.100000           1.800000
max              7.900000           4.400000            6.900000           2.500000

"""
