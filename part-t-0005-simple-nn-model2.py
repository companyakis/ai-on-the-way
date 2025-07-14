profit_forecast_model.bias = nn.Parameter(torch.tensor([-30000.0]))

profit_forecast_model.weight = nn.Parameter(torch.tensor([2.0]))

print(profit_forecast_model.bias)

print(profit_forecast_model.weight)

"""
Parameter containing:
tensor([-30000.], requires_grad=True)

Parameter containing:
tensor([2.], requires_grad=True)

"""
