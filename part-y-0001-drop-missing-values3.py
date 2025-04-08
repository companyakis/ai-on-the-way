dropped_data = data.dropna()

print(dropped_data.isnull().sum())

"""
Age         0
Shape       0
Margin      0
Density     0
Severity    0
dtype: int64

"""
