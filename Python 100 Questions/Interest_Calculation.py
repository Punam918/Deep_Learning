# Function to calculate simple interest
def calculate_simple_interest(principal, rate_of_interest, time_period):
    interest = (principal * rate_of_interest * time_period) / 100
    return interest

# Example input
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

# Output the simple interest
simple_interest = calculate_simple_interest(principal, rate_of_interest, time_period)
print(f"The simple interest is: {simple_interest:.2f}")
