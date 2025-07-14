import torch
from torch import nn 

# profit = 2 * sales - 300
# y = 2 * X - 30000
# first_quarter_sales = torch.tensor([55_600, 62_000, 48_600])
# fixed_cost_per_month = torch.tensor(30_000)

X = torch.tensor([
    [55_600],
    [62_000],
    [48_600]
])

profit_forecast_model = nn.Linear(1, 1)

print(profit_forecast_model) # inear(in_features=1, out_features=1, bias=True)
