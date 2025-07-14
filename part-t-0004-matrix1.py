import torch
import numpy as np

np.random.seed(2025)

quarterly_sales_by_months = torch.tensor([
    [np.random.randint(25000, 45000), np.random.randint(25000, 45000), np.random.randint(25000, 45000)],
    [np.random.randint(25000, 45000), np.random.randint(25000, 45000), np.random.randint(25000, 45000)],
    [np.random.randint(25000, 45000), np.random.randint(25000, 45000), np.random.randint(25000, 45000)],
    [np.random.randint(25000, 45000), np.random.randint(25000, 45000), np.random.randint(25000, 45000)]
])

print(f"Sales data: {quarterly_sales_by_months}")

"""
Sales data: tensor([[41338, 36102, 40948],
        [41707, 30331, 36768],
        [40845, 26034, 34422],
        [44685, 26381, 34428]])

"""
