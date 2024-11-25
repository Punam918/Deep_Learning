# Function to calculate factorial using recursive approach
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Input: Taking the number from the user
number = int(input("Enter a number: "))

# Calculate and display the factorial
fact = factorial_recursive(number)
print(f"The factorial of {number} is: {fact}")
