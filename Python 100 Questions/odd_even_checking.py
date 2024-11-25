# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example input
number = int(input("Enter a number: "))

# Output whether the number is odd or even
result = check_odd_even(number)
print(f"The number {number} is {result}.")
