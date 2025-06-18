import torch

# profit = 2 * sales - 300

# y = 2 * X - 30_000

sales_january = torch.tensor(55_600)

initial_cost = torch.tensor(30_000)

profit = 2 * sales_january - initial_cost

print(profit) # tensor(81200)




