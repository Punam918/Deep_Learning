# Function to calculate profit or loss
def calculate_profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        profit = selling_price - cost_price
        return f"Profit of {profit}"
    elif cost_price > selling_price:
        loss = cost_price - selling_price
        return f"Loss of {loss}"
    else:
        return "No profit, no loss"

# Example input
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Output the result
result = calculate_profit_or_loss(cost_price, selling_price)
print(result)
