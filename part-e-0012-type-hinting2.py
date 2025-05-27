def sales_profit_loss(sales: int | float, cost: int | float) -> int | float:
    
    return sales - cost

print("Quarter 1 profit or loss: ", sales_profit_loss(5200, 4300))

print("Quarter 2 profit or loss: ", sales_profit_loss(3200.16, 4300))


# Quarter 1 profit or loss:  900
# Quarter 2 profit or loss:  -1099.8400000000001
