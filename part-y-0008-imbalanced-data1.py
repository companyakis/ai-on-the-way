import pandas as pd

df = pd.read_csv("./diabetes.csv")

print(df.columns)

print("--------------------------------------------")

print(df["Outcome"].value_counts())

print("--------------------------------------------")

print(df["Outcome"].value_counts(normalize = True))

"""
Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
      dtype='object')
--------------------------------------------
Outcome
0    500
1    268
Name: count, dtype: int64
--------------------------------------------
Outcome
0    0.651042
1    0.348958
Name: proportion, dtype: float64

"""
