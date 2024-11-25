'''Write a program that will reverse a four digit number.Also it checks
whether the reverse is true.'''

# Function to reverse a four-digit number
def reverse_number(number):
    reversed_num = int(str(number)[::-1])
    return reversed_num

# Function to check if the reverse is equal to the original number
def is_palindrome(number):
    reversed_num = reverse_number(number)
    return number == reversed_num

# Example input
number = int(input("Enter a four-digit number: "))

# Reverse the number
reversed_num = reverse_number(number)

# Output the reversed number
print(f"The reversed number is: {reversed_num}")

# Check if the reverse is equal to the original number
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
