# Function to print the pattern
def pattern5():
    num = 1
    for i in range(1, 5):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# Print the pattern
pattern5()
