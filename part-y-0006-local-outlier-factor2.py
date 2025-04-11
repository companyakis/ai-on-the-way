import pandas as pd

data = pd.read_csv("diabetes.csv")

data_shape = data.shape

print(data_shape) # (768, 9)

print("----------------------------------------")

X = data.iloc[:, 0:(data_shape[1] - 1)]

print(X.columns)

print("----------------------------------------")

y = data.iloc[:, data_shape[1] - 1]

print(pd.DataFrame(y).value_counts(normalize = True))

"""
(768, 9)
----------------------------------------
Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'],
      dtype='object')
----------------------------------------
Outcome
0          0.651042
1          0.348958
Name: proportion, dtype: float64

"""
