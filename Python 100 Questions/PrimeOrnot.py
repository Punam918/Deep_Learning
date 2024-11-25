def primeornot(num):
        # Prime numbers must be greater than 1
    if num <= 1:
        return False
    # Check for factors from 2 to sqrt(n)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#input
number = int(input("Enter any number:"))

result = primeornot(number)
print(f"The given number {number} is {result}")