# Function to count the number of digits in a number
def count_digits(n):
    return len(str(n))

# Input: Taking the number from the user
number = int(input("Enter a number: "))

# Count and display the number of digits
num_digits = count_digits(number)
print(f"The number of digits in {number} is: {num_digits}")
