# Function to find HCF of two numbers
def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Input: Taking two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the HCF
hcf = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf}")

# Function to find LCM of two numbers
def find_lcm(a, b):
    hcf = find_hcf(a, b)
    return (a * b) // hcf

# Input: Taking two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the LCM
lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
