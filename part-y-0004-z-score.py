import pandas as pd
from sklearn.preprocessing import StandardScaler

iris = pd.read_csv("./iris/iris.data", names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

x = iris.iloc[:, :4]

y = iris.iloc[:, -1]

scaler = StandardScaler()

"""
z-score
scaled_x = (x - mean(x))/ std(x) 
"""

scaled_x = scaler.fit_transform(x)

scaled_df = pd.DataFrame(scaled_x, columns = x.columns)

print(scaled_df.head())

print(scaled_df.describe())

"""
   sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
0           -0.900681           1.032057           -1.341272          -1.312977
1           -1.143017          -0.124958           -1.341272          -1.312977
2           -1.385353           0.337848           -1.398138          -1.312977
3           -1.506521           0.106445           -1.284407          -1.312977
4           -1.021849           1.263460           -1.341272          -1.312977

       sepal length in cm  sepal width in cm  petal length in cm  petal width in cm
count        1.500000e+02       1.500000e+02        1.500000e+02       1.500000e+02
mean        -4.736952e-16      -6.631732e-16        3.315866e-16      -2.842171e-16
std          1.003350e+00       1.003350e+00        1.003350e+00       1.003350e+00
min         -1.870024e+00      -2.438987e+00       -1.568735e+00      -1.444450e+00
25%         -9.006812e-01      -5.877635e-01       -1.227541e+00      -1.181504e+00
50%         -5.250608e-02      -1.249576e-01        3.362659e-01       1.332259e-01
75%          6.745011e-01       5.692513e-01        7.627586e-01       7.905908e-01
max          2.492019e+00       3.114684e+00        1.786341e+00       1.710902e+00

"""
