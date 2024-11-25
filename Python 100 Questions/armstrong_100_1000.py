# Function to check if a number is an Armstrong number
def is_armstrong(n):
    # Convert the number to a string and find its digits
    digits = [int(digit) for digit in str(n)]
    
    # Calculate the sum of the cubes of its digits
    sum_of_cubes = sum(digit ** 3 for digit in digits)
    
    # Return True if the sum of cubes is equal to the number itself
    return n == sum_of_cubes

# Loop through the range from 100 to 1000
print("Armstrong numbers between 100 and 1000 are:")
for num in range(100, 1000):
    if is_armstrong(num):
        print(num, end=' ')
