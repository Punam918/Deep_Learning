# Function to calculate the sum of squares of three digits
def sum_of_squares(digit1, digit2, digit3):
    return digit1**2 + digit2**2 + digit3**2

# Input: Taking three digits from the user
digit1 = int(input("Enter the first digit: "))
digit2 = int(input("Enter the second digit: "))
digit3 = int(input("Enter the third digit: "))

# Calculate the sum of the squares
result = sum_of_squares(digit1, digit2, digit3)

# Output: Display the result
print(f"The sum of squares of {digit1}, {digit2}, and {digit3} is: {result}")
