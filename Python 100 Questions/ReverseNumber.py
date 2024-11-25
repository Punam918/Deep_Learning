# Function to reverse a number
def reverse_number(n):
    return int(str(n)[::-1])

# Input: Taking the number from the user
number = int(input("Enter a number: "))

# Find and display the reversed number
reversed_number = reverse_number(number)
print(f"The reverse of {number} is: {reversed_number}")
