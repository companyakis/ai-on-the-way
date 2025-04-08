data_new = data.copy()

imputer = imputer.fit(data_new)

data_new = imputer.transform(data_new)

print(type(data_new)) # <class 'numpy.ndarray'>

data_new = pd.DataFrame(data_new, columns = columns)

print(data_new.isnull().sum())

"""
<class 'numpy.ndarray'>
BI-RADS     0
Age         0
Shape       0
Margin      0
Density     0
Severity    0
dtype: int64

"""

print(data.isnull().sum())

"""
BI-RADS      2
Age          5
Shape       31
Margin      48
Density     76
Severity     0
dtype: int64

"""
