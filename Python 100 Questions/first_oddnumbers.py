# Function to print the first n odd numbers
def print_odd_numbers(n):
    count = 0
    number = 1
    while count < n:
        print(number, end=' ')
        number += 2
        count += 1
    print()  # To ensure the output ends with a newline

# Number of odd numbers to print
n = 25

# Print the first 25 odd numbers
print_odd_numbers(n)
