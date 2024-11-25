# Function to calculate the sum of first n natural numbers
def sum_of_n_numbers(n):
    return n * (n + 1) // 2  # Formula for the sum of first n numbers: n*(n+1)/2

# Input: Taking the value of n from the user
n = int(input("Enter a number (n): "))

# Calculate and display the sum of first n numbers
sum_n = sum_of_n_numbers(n)
print(f"The sum of the first {n} numbers is: {sum_n}")
