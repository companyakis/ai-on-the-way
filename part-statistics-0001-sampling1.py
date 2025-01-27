import numpy as np

np.random.seed(2025)

people_ages = np.random.randint(0, 95, 5000)

print(people_ages[10], people_ages[98], people_ages[1012]) # 10 60 87
