# Function to compute n + nn + nnn
def compute_n_expression(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    return n + nn + nnn

# Input: Taking the number from the user
n = int(input("Enter an integer: "))

# Compute and display the result
result = compute_n_expression(n)
print(f"The result of n + nn + nnn is: {result}")
