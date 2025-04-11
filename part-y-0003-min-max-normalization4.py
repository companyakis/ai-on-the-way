import pandas as pd
from sklearn.preprocessing import MinMaxScaler

iris = pd.read_csv("./iris/iris.data", names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

x = iris.iloc[:, :4]

y = iris.iloc[:, -1]

scaler = MinMaxScaler(feature_range = (0, 1))

scaled_x = scaler.fit_transform(x)

scaled_df = pd.DataFrame(scaled_x, columns = x.columns)

print(scaled_df.head())

print(scaled_df.describe())

"""
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
0            0.222222           0.625000            0.067797           0.041667
1            0.166667           0.416667            0.067797           0.041667
2            0.111111           0.500000            0.050847           0.041667
3            0.083333           0.458333            0.084746           0.041667
4            0.194444           0.666667            0.067797           0.041667

       sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
count          150.000000         150.000000          150.000000         150.000000
mean             0.428704           0.439167            0.467571           0.457778
std              0.230018           0.180664            0.299054           0.317984
min              0.000000           0.000000            0.000000           0.000000
25%              0.222222           0.333333            0.101695           0.083333
50%              0.416667           0.416667            0.567797           0.500000
75%              0.583333           0.541667            0.694915           0.708333
max              1.000000           1.000000            1.000000           1.000000
"""
