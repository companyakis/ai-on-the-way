import pandas as pd

iris = pd.read_csv("./iris/iris.data", names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

print(iris["class"].value_counts())

"""
class
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Name: count, dtype: int64

"""

x = iris.iloc[:, :4]

y = iris.iloc[:, -1]
