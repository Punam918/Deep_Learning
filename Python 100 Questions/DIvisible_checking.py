# Function to check if a number is divisible by 3 and 6
def check_divisibility(number):
    if number % 3 == 0 and number % 6 == 0:
        return "The number is divisible by both 3 and 6."
    elif number % 3 == 0:
        return "The number is divisible by 3 but not by 6."
    elif number % 6 == 0:
        return "The number is divisible by 6 but not by 3."
    else:
        return "The number is neither divisible by 3 nor by 6."

# Example input
number = int(input("Enter a number: "))

# Output the result
result = check_divisibility(number)
print(result)
