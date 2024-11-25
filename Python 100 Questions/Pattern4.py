# Function to print the pattern
def pattern4(n):
    for i in range(1, n + 1):
        # Print the first half (1 to i)
        for j in range(1, i + 1):
            print(j, end=" ")
        # Print the second half (i-1 to 1)
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()

# Print the pattern
pattern4(5)
