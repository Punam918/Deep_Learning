# Function to print first 20 Fibonacci numbers
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Print the first 20 Fibonacci numbers
fibonacci_series(20)
