def swapnumber(n1,n2):
    n1,n2 = n2,n1
    return n1,n2
#input
n1 = int(input("Enter the First number: "))
n2 = int(input("Enter the Secong number: "))

#output
num1,num2 = swapnumber(n1,n2)
print(f"The First number after swapping becomes {num1}and Second number becomes {num2}")
