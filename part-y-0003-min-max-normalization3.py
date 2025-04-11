import pandas as pd
from sklearn.preprocessing import MinMaxScaler

iris = pd.read_csv("./iris/iris.data", names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

x = iris.iloc[:, :4]

y = iris.iloc[:, -1]

scaler = MinMaxScaler(feature_range = (0, 1))

scaled_x = scaler.fit_transform(x)

print(type(scaled_x)) # <class 'numpy.ndarray'>

print(scaled_x[:5])

"""
[[0.22222222 0.625      0.06779661 0.04166667] 
 [0.16666667 0.41666667 0.06779661 0.04166667] 
 [0.11111111 0.5        0.05084746 0.04166667] 
 [0.08333333 0.45833333 0.08474576 0.04166667] 
 [0.19444444 0.66666667 0.06779661 0.04166667]]

"""
