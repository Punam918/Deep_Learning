# Function to check if a number is a Narcissistic number
def is_narcissistic(number):
    # Convert the number to a string to access each digit
    digits = str(number)
    
    # Ensure the number is 4 digits
    if len(digits) != 4:
        return False

    # Calculate the sum of each digit raised to the power of 4 (since it's a 4-digit number)
    narcissistic_sum = sum(int(digit) ** 4 for digit in digits)
    
    # Check if the sum is equal to the original number
    return narcissistic_sum == number

# Input: Taking a 4-digit number from the user
number = int(input("Enter a 4-digit number: "))

# Check and display whether the number is a Narcissistic number or not
if is_narcissistic(number):
    print(f"{number} is a Narcissistic number.")
else:
    print(f"{number} is not a Narcissistic number.")
