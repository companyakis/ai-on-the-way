import pandas as pd
import numpy as np

columns =["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

from google.colab import files
uploaded = files.upload()

data = pd.read_csv("mammographic_masses.data", names=columns, na_values=["?"])

print(data.head())

"""
   BI-RADS   Age  Shape  Margin  Density  Severity
0      5.0  67.0    3.0     5.0      3.0         1
1      4.0  43.0    1.0     1.0      NaN         1
2      5.0  58.0    4.0     5.0      3.0         1
3      4.0  28.0    1.0     1.0      3.0         0
4      5.0  74.0    1.0     5.0      NaN         1

"""
