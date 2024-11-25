# Function to multiply two numbers using repeated addition
def multiply(a, b):
    # Determine the sign of the result
    negative = (a < 0) ^ (b < 0)
    
    # Work with absolute values to simplify the multiplication process
    a, b = abs(a), abs(b)
    
    result = 0
    for _ in range(b):
        result += a
    
    # Adjust the sign of the result if necessary
    if negative:
        result = -result
    
    return result

# Input: Taking two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform multiplication
product = multiply(num1, num2)

# Output: Display the result
print(f"The product of {num1} and {num2} is: {product}")
