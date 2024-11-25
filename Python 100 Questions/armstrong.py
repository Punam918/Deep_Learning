# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to easily iterate over digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Input: Taking a number from the user
number = int(input("Enter a number: "))

# Check and display whether the number is an Armstrong number or not
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
