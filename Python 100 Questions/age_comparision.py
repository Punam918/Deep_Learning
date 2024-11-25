def findOldestage(age1,age2,age3):
    return max(age1,age2,age3)

#Taking input
age1 = int(input("Enter the first age:"))
age2 = int(input("Enter the second age:"))
age3 = int(input("Enter the Third age:"))

#output
oldest = findOldestage(age1,age2,age3)
print(f"The oldest age amoung all these is {oldest}")
