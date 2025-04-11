import pandas as pd

from imblearn.over_sampling import SMOTE

df = pd.read_csv("./diabetes.csv")

X = df.iloc[:, 0:8]

y = df.iloc[:, -1]

strategy = SMOTE()

X, y = strategy.fit_resample(X, y)

new_df = pd.concat([X, y], axis=1)

print(new_df["Outcome"].value_counts())

print(new_df.shape)

print("--------------------------------------------")

print(df["Outcome"].value_counts())

print(df.shape)

"""
Outcome
1    500
0    500
Name: count, dtype: int64

(1000, 9)
--------------------------------------------
Outcome
0    500
1    268
Name: count, dtype: int64

(768, 9)

"""
