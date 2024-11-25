# Function to print the pattern
def pattern2(n):
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Print the pattern
pattern2(3)
