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
], dtype = torch.float32)

profit_forecast_model = nn.Linear(1, 1)

profit_forecast_model.bias = nn.Parameter(torch.tensor([-30_000], dtype = torch.float32))

profit_forecast_model.weight = nn.Parameter(torch.tensor([[2]], dtype = torch.float32))

profit_predictions = profit_forecast_model(X)

print(profit_predictions)

"""
tensor([[81200.],
        [94000.],
        [67200.]], grad_fn=<AddmmBackward0>)

"""
