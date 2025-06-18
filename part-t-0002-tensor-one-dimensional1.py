import torch

# profit = 2 * sales - 30000

# y = 2 * X - 30_000

first_quarter_sales = torch.tensor([55_600, 62_000, 48_600])

fixed_cost_per_month = torch.tensor(30_000)

profit = 2 * first_quarter_sales - fixed_cost_per_month

print(profit) # tensor([81200, 94000, 67200])




