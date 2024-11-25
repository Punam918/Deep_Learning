def sumofdigits(n1,n2,n3):
    return n1+n2+n3

#input
num1 = int(input("First number:"))
num2 = int(input("Second number:"))
num3 = int(input("Third number:"))


#output
total = sumofdigits(num1,num2,num3)
print(f"The sum of digits provided becomes {total}")